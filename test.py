import subprocess
import tempfile
import os

def compile_jsx_npx(jsx_code: str) -> str:
    with tempfile.NamedTemporaryFile(mode='w+', suffix=".jsx", delete=False) as temp_input:
        temp_input.write(jsx_code)
        temp_input_path = temp_input.name

    temp_output_path = temp_input_path.replace('.jsx', '.js')

    try:
        subprocess.run(
            [
                "npx", "babel",
                temp_input_path,
                "--out-file", temp_output_path,
                "--presets", "@babel/preset-react"
            ],
            check=True,
            capture_output=True,
            text=True
        )

        with open(temp_output_path, "r") as f:
            compiled_js = f.read()

        compiled_js = compiled_js.lstrip('"use strict";').strip().rstrip(';')

        return compiled_js

    except subprocess.CalledProcessError as e:
        print("Error running Babel:", e.stderr)
        return None

    finally:
        os.remove(temp_input_path)
        if os.path.exists(temp_output_path):
            os.remove(temp_output_path)

def test_jsx_template(jsx_code: str, json_data: any) -> bool:
    compiled = compile_jsx_npx(jsx_code)
    if compiled is None:
        return False
    
    with open('test.js', 'w') as f:
        f.write(compiled)

    try:
        subprocess.run(
            ["node", "test.js"],
            check=True,
            capture_output=True,
            text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print("Error running test.js:", e.stderr)
        return False

# Example JSX
jsx_code = """
<div>Hello, {props.name}</div>
"""

compiled = test_jsx_template(jsx_code, {"name": "John Doe"})
print(compiled)
