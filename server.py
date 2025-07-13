from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from llm_tester import json_to_lcars_node, model, json_to_lcars_html, random_json, json_to_lcars_jsx, reorganize_json
from fastapi.responses import FileResponse
import json
import httpx
from fastapi import Response
from fastapi.responses import JSONResponse

import asyncio

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")

@app.get("/random_json")
async def random_json_ep(url: str = None):
    if url:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()

    res = random_json(model)
    return res

@app.post("/convert")
async def convert_json(data: dict):
    try:
        lcars_structure = json_to_lcars_node(data, model)
        return lcars_structure
    except Exception as e:
        return {"error": str(e)}


@app.post("/reorganize_json")
async def reorganize_json_ep(data: dict):
    lcars_structure = reorganize_json(data, model)
    return lcars_structure


@app.post("/generate_html", response_class=HTMLResponse)
async def generate_html(data: dict):
    try:
        html_output = json_to_lcars_html(data, model)
        return html_output
    except Exception as e:
        return f"<div class='error'>Error: {str(e)}</div>"


@app.post("/generate_jsx", response_class=HTMLResponse)
async def generate_jsx(data: dict):
    # Cache the result for subsequent requests
    # if hasattr(generate_jsx, '_cached_result'):
    #     return generate_jsx._cached_result
    try:
        jsx_output = json_to_lcars_jsx(data, model)
        generate_jsx._cached_result = jsx_output
        return jsx_output
    except Exception as e:
        return f"<div class='error'>Error: {str(e)}</div>"


@app.post("/save_template/{name}")
async def save_template(name: str, template: str):
    try:
        with open(f"static/{name}.jsx", "w") as f:
            f.write(template)
        return {"status": "success", "message": f"Template saved successfully as {name}.jsx"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


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



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006, timeout_keep_alive=60)
