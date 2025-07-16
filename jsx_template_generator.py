from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from typing import TypedDict
import json
import subprocess
import os
import tempfile

model = ChatOpenAI(
    base_url="http://cluster:32605/v1",
    # model="llama3.2:3b",
    # model="deepseek-r1:14b",
    model="gemma3:27b",  # favorite so far
    # model="qwen3:14b",
    # model="phi4-mini:3.8b",
    # model="phi3:14b",
    # model="mistral:7b",
    # model="tinyllama",
    # model="openhermes:latest",
    # model="",
    temperature=0.7,
    max_retries=3,
    timeout=1000,
)

# model = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0.7,
#     max_retries=3,
#     timeout=1000,
# )

from typing import TypedDict, Literal, List, Union, Optional




def extract_markdown_block(text: str, type: str) -> str:
    if '```' not in text:
        print(f"extract_markdown_block: no ``` found in: {text}")
        return text
    if f"```{type}" in text:
        print(f"extract_markdown_block: found ```{type} in: {text}")
        return text.split(f"```{type}", 1)[1].split("```")[0]
    print(f"extract_markdown_block: found ``` but not ```{type} in: {text}")
    return text.split("```", 1)[1].split("```")[0]


def extract_jsx_from_react_component(jsx_template: str) -> str:
    if "function" in jsx_template and "return" in jsx_template:
        try:
            # Find the JSX between return and the closing brace
            start = jsx_template.find("return") + 6  # Skip "return"
            end = jsx_template.rfind("}")
            if start > 6 and end > start:
                jsx_template = jsx_template[start:end].strip()
        except:
            pass

    jsx_template = jsx_template.strip()#.lstrip("(").rstrip(");")

    return jsx_template


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

        compiled_js = compiled_js.split("\n", 2)[2]

        return compiled_js

    except subprocess.CalledProcessError as e:
        print("Error running Babel:", e.stderr)
        return None

    finally:
        os.remove(temp_input_path)
        if os.path.exists(temp_output_path):
            os.remove(temp_output_path)


JSX_GEN_PROMPT = """
Generate a JSX template to render the following JSON data:

```json
{}
```

Only return the JSX template. Do not include the React component or javascript. Just the JSX template.
Do not include any <script> or <style> tags. 
Assume the the JSON is passed as a paramter called `props`. For example, if you have {{ "name": "Joe" }}, you should use `props.name` in the JSX template.
Consider using cards, flexboxes, tables, lists, and other css properties to make it look really cool.

Use inline styles to make the UI look like a LCARS interface from the Star Trek The Next Generation. 
Always render groups of numbers as progress bars and gauges, add the original numbers in the center of the progress bar.
If the values of numbers are very large, use M, G, T, P, E, Z, Y, etc. If they are very small, use m, u, n, p, f, a, z, y, etc.
Organize the information into groups and sections. 
This template will be rendered as one component in a React application. It should not take up the whole screen. Come up with a component that is easy to drop into a page.
To fit more things on the screen, make everything smaller and concise, use text-overflow: ellipsis.

Try to include all of the information from the JSON in the JSX template. We don't want to lose information.
Never use `JSON.stringify` in the JSX template. Do not use `JSON.stringify`. Don't use `JSON.stringify`.
The optional chaining operator is not available. Do not use `props.contact?.email`, you must write `props.contact && props.contact.email`.
"""


# JSX_GEN_PROMPT = """
# Generate a JSX template to render the following JSON data:

# ```json
# {}
# ```

# Only return the JSX template. Do not include the React component or javascript. Just the JSX template.
# Do not include any <script> or <style> tags. 
# Assume the the JSON is passed as a paramter called `props`. For example, if you have {{ "name": "Joe" }}, you should use `props.name` in the JSX template.
# Consider using cards, flexboxes, tables, lists, and other css properties to make it look really cool.

# Use css classes from the Twitter Bootstrap CSS framework.
# Always render groups of numbers as progress bars and gauges, add the original numbers in the center of the progress bar.
# Organize the information into groups and sections. 
# This template will be rendered as one component in a React application. It should not take up the whole screen. Come up with a component that is easy to drop into a page.
# To fit more things on the screen, make everything smaller and concise, use text-overflow: ellipsis.

# Try to include all of the information from the JSON in the JSX template. We don't want to lose information.
# Never use `JSON.stringify` in the JSX template. Do not use `JSON.stringify`. Don't use `JSON.stringify`.
# The optional chaining operator is not available. Do not use `props.contact?.email`, you must write `props.contact && props.contact.email`.
# """

# JSX_GEN_PROMPT = """
# You are generating a compact, professional-looking ReactJS JSX component to visualize structured JSON data based on the following data:

# ```json
# {}
# ```

# Only return the JSX template. Do not include the React component or javascript. Just the JSX template.
# Do not include any <script> or <style> tags. 
# Assume the the JSON is passed as a paramter called `props`. For example, if you have {{ "name": "Joe" }}, you should use `props.name` in the JSX template.


# Your goals:
# - Use pre-existing css classes from the Twitter Bootstrap CSS framework.
# - Use clean, modern UI patterns: cards, tables, flex layouts, and lists.
# - Group related data into clearly labeled sections or cards for visual hierarchy.
# - For numeric values or metric groups, render progress bars or gauges, placing the raw number visibly inside the bar or nearby.
# - Keep the layout compact: small font sizes, tight spacing, and use `text-overflow: ellipsis` for overflow-prone text.
# - Ensure the component is self-contained, does **not take up the full screen**, and is visually balanced for embedding in a larger UI.
# - Prioritize readability and aesthetic structure. Use icons or subtle separators to break up dense information.
# - Make smart choices about what to emphasize or collapse if the data is long or nested.
# - Prefer rendering the data in a way that is easy to read and understand.
# - Rendering related things together.

# The final JSX should be clean, readable, and immediately usable as a drop-in React component.


# Try to include all of the information from the JSON in the JSX template. We don't want to lose information.
# Never use `JSON.stringify` in the JSX template. Do not use `JSON.stringify`. Don't use `JSON.stringify`.
# The optional chaining operator is not available. Do not use `props.contact?.email`, you must write `props.contact && props.contact.email`.
# """

def get_jsx_template(json_data: any, llm: any, retries: int = 20):
    """
    check if a matching template exists in the template cache
    use heuristics based on the keys of the json data
    if a matching template is found:
        return the matching template
    """
    simple_checks = [ 'JSON.stringify', '<style' ]

    prompt = JSX_GEN_PROMPT.format(json.dumps(json_data, indent=2))

    for i in range(retries):
        jsx_template = None

        for i in range(retries):
            res = llm.invoke(prompt).content  # generate with the LLM

            # check for simple errors
            for check in simple_checks:
                if check in res:
                    print(f'llm gave us a {check}, skipping')
                    continue

            # attempt to extract the JSX template
            try:
                jsx_template = extract_markdown_block(res, "jsx")
                if jsx_template:
                    break
            except:
                pass

        if not jsx_template:
            raise Exception("Failed to generate valid JSX")

        try:
            jsx_template = extract_jsx_from_react_component(jsx_template)
            return jsx_template
            # compiled_jsx_template = compile_jsx_npx(jsx_template)
            # return compiled_jsx_template
        except:
            pass

    raise Exception("Failed to generate valid JSX")













if __name__ == "__main__":
    some_json = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "contact": {
            "email": "john.doe@starfleet.org",
            "phone": "555-0123",
            "address": {
                "street": "123 Main St",
                "zip": "10001",
                "country": "United States"
            }
        },
        "assignments": [
            {
                "ship": "USS Enterprise",
                "role": "Science Officer",
                "startDate": "2360-03-15"
            },
            {
                "ship": "USS Voyager", 
                "role": "Chief Medical Officer",
                "startDate": "2371-01-20"
            }
        ],
        "skills": ["xenobiology", "astrophysics", "medical research"],
        "certifications": ["Starfleet Medical", "Advanced Xenoscience"]
    }

    # jsx = get_jsx_template(some_json, model)
    jsx = """
<div>
    <h1>{props.name}</h1>
    <p>Age: {props.age}</p>
    <p>City: {props.city}</p>
    <p>Email: {props.contact.email}</p>
</div>
"""
    print(jsx)

