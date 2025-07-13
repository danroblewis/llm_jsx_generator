from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from llm_tester import json_to_lcars_node, model, json_to_lcars_html, random_json, json_to_lcars_jsx, reorganize_json
from fastapi.responses import FileResponse
import json

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")

@app.get("/random_json")
async def random_json_ep():
    # Cache the result for subsequent requests
    # if hasattr(random_json_ep, '_cached_result'):
    #     return random_json_ep._cached_result

    res = random_json(model)
    random_json_ep._cached_result = res

    # with open("kubeshit.json", "r") as f:
    #     res = json.load(f)
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006, timeout_keep_alive=60)
