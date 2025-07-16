from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jsx_template_generator import get_jsx_template, model
from fastapi.responses import FileResponse
import json
import httpx
from fastapi import Response
from fastapi.responses import JSONResponse
import asyncio
import hashlib
import os
import aiohttp


JSX_TEMPLATE_DIR = "jsx_template_cache"


def generate_json_structure_hash(data: dict) -> str:
    """
    Generate a hash based only on the keys and structure of a JSON object.
    Recursively processes nested dictionaries and lists.
    """
    def process_structure(obj) -> str:
        if isinstance(obj, dict):
            # Sort keys to ensure consistent ordering
            return f"dict({','.join(sorted(k + process_structure(v) for k, v in obj.items()))})"
        elif isinstance(obj, list):
            if not obj:
                return "list()"
            # For lists, we only care about the structure of the first item
            return f"list({process_structure(obj[0])})"
        else:
            # For primitive types, we only care about their type
            return type(obj).__name__
    
    structure_str = process_structure(data)
    return hashlib.sha256(structure_str.encode()).hexdigest()


app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.new.html")


@app.post("/get_jsx_template", response_class=HTMLResponse)
async def get_jsx_template_ep(data: dict, regenerate: bool = False):
    # Return loading div if data is empty
    if not data:
        return '<div>Loading...</div>'

    data_hash = generate_json_structure_hash(data)
    template_path = os.path.join(JSX_TEMPLATE_DIR, f"{data_hash}.jsx")
    print(f"using template: {template_path}")

    # use cache if it exists
    if os.path.exists(template_path) and not regenerate:
        with open(template_path, 'r') as f:
            return f.read()

    template = get_jsx_template(data, model)

    # save the new template to the template cache
    with open(template_path, 'w') as f:
        f.write(template)

    return template



@app.get("/proxy")
async def proxy(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers)
            )
    except Exception as e:
        return {"error": str(e)}


@app.get("/random_json")
async def random_json_ep(url: str = None):
    try:
        # Get CPU info from /proc/stat
        with open('/proc/stat', 'r') as f:
            cpu_line = f.readline().split()
            total = sum(float(i) for i in cpu_line[1:])
            idle = float(cpu_line[4])
            cpu_percent = 100 * (1 - idle/total)

        # Get memory info from /proc/meminfo
        mem_info = {}
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                key, value = line.split(':')
                value = int(value.strip().split()[0]) * 1024 # Convert KB to bytes
                mem_info[key] = value

        # Get disk info using df command
        import subprocess
        df = subprocess.check_output(['df', '/']).decode().split('\n')[1].split()
        total_disk = int(df[1]) * 1024
        used_disk = int(df[2]) * 1024
        free_disk = int(df[3]) * 1024
        disk_percent = int(df[4].rstrip('%'))

        # Get system uptime
        with open('/proc/uptime', 'r') as f:
            uptime = float(f.readline().split()[0])

        # Get load averages
        with open('/proc/loadavg', 'r') as f:
            load = f.readline().split()
            load_1min = float(load[0])
            load_5min = float(load[1])
            load_15min = float(load[2])

        # Get network stats
        with open('/proc/net/dev', 'r') as f:
            net_stats = {}
            lines = f.readlines()
            for line in lines[2:]:  # Skip header lines
                interface = line.split(':')[0].strip()
                if interface != 'lo':  # Skip loopback
                    values = line.split(':')[1].split()
                    net_stats[interface] = {
                        'bytes_received': int(values[0]),
                        'packets_received': int(values[1]),
                        'bytes_sent': int(values[8]),
                        'packets_sent': int(values[9])
                    }

        stats = {
            "cpu": {
                "percent_used": round(cpu_percent, 1),
                "load_averages": {
                    "1min": load_1min,
                    "5min": load_5min,
                    "15min": load_15min
                }
            },
            "memory": {
                "total": mem_info['MemTotal'],
                "available": mem_info['MemAvailable'],
                "used": mem_info['MemTotal'] - mem_info['MemAvailable'],
                "free": mem_info['MemFree'],
                "percent_used": round((1 - mem_info['MemAvailable']/mem_info['MemTotal']) * 100, 1),
                "swap_total": mem_info.get('SwapTotal', 0),
                "swap_free": mem_info.get('SwapFree', 0),
                "cached": mem_info.get('Cached', 0),
                "buffers": mem_info.get('Buffers', 0)
            },
            "disk": {
                "total": total_disk,
                "used": used_disk,
                "free": free_disk, 
                "percent_used": disk_percent
            },
            "uptime": {
                "seconds": uptime,
                "days": round(uptime / 86400, 2),
                "hours": round(uptime / 3600, 2)
            }
        }

        return JSONResponse(content=stats)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.get("/kubectl_json")
async def kubectl_json(command: str):
    try:
        # Add -o json to the command if not present
        if "-o json" not in command:
            command += " -o json"
            
        # Run kubectl command and capture output
        process = await asyncio.create_subprocess_shell(
            f"kubectl {command}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            return JSONResponse(
                status_code=400,
                content={"error": stderr.decode()}
            )

        # Parse JSON output
        json_output = json.loads(stdout.decode())
        return json_output

    except json.JSONDecodeError:
        return JSONResponse(
            status_code=400, 
            content={"error": "Invalid JSON output from kubectl command"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.get("/openwrt_prometheus_metrics")
async def openwrt_prometheus_metrics():
    # Make request to Prometheus metrics endpoint
    async with aiohttp.ClientSession() as session:
        async with session.get('http://10.198.1.1:9100/metrics') as response:
            if response.status != 200:
                return JSONResponse(
                    status_code=response.status,
                    content={"error": "Failed to fetch metrics"}
                )
            
            text = await response.text()

    # Parse metrics into JSON structure
    metrics = {}
    current_metric = None
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('# TYPE'):
            # Extract metric name and type
            parts = line.split(' ')
            if len(parts) >= 3:
                metric_name = parts[2]
                metric_type = parts[3] if len(parts) > 3 else 'unknown'
                metrics[metric_name] = {
                    'type': metric_type,
                    'values': []
                }
                current_metric = metric_name
            
        elif not line.startswith('#'):
            # Parse metric value line
            parts = line.split(' ')
            if len(parts) >= 2:
                metric_name = parts[0]
                base_name = metric_name.split('{')[0]
                try:
                    value = float(parts[-1])
                except ValueError:
                    continue
                
                if base_name not in metrics:
                    metrics[base_name] = {
                        'type': 'unknown',
                        'values': []
                    }
                
                labels = {}
                if '{' in metric_name:
                    # Extract labels
                    labels_str = metric_name[metric_name.find('{')+1:metric_name.find('}')]
                    for label_pair in labels_str.split(','):
                        if '=' in label_pair:
                            k, v = label_pair.split('=', 1)
                            labels[k] = v.strip('"')
                        
                metrics[base_name]['values'].append({
                    'labels': labels,
                    'value': value
                })

    return JSONResponse(content=metrics)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006, timeout_keep_alive=60)


