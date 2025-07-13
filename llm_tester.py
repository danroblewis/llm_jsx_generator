from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from typing import TypedDict
import json



model = ChatOpenAI(
    base_url="http://cluster:32605/v1",
    # model="llama3.2:3b",
    # model="deepseek-r1:14b",
    model="gemma3:27b",
    temperature=0.7,
    max_tokens=1000,
    max_retries=3,
    timeout=1000,
)


"""

I want this project to take an arbitrary JSON structure and produce an LCARS display of the data.

I need a dynamic structure. 




"""




from typing import TypedDict, Literal, List, Union, Optional

# Base styles and positioning
class LCARSDimensions(TypedDict, total=False):
    width: Optional[int]
    height: Optional[int]
    x: Optional[int]
    y: Optional[int]

class LCARSStyle(TypedDict, total=False):
    color: Optional[str]  # hex or LCARS color token
    shape: Optional[Literal["rounded", "rect", "pill"]]
    alignment: Optional[Literal["left", "right", "center"]]
    emphasis: Optional[Literal["normal", "highlight", "alert", "muted"]]
    font_size: Optional[int]

# Base component
class LCARSComponent(TypedDict):
    id: str
    type: str
    title: Optional[str]
    dimensions: Optional[LCARSDimensions]
    style: Optional[LCARSStyle]

# Text component (readout, label)
class LCARSText(LCARSComponent):
    type: Literal["text"]
    text: str

# Button or interactive area
class LCARSButton(LCARSComponent):
    type: Literal["button"]
    label: str
    action: Optional[str]  # semantic or literal action like "navigate:/status"

# Grouping container (row, column, stack, grid)
class LCARSContainer(LCARSComponent):
    type: Literal["container"]
    layout: Literal["vertical", "horizontal", "grid"]
    children: List["LCARSNode"]  # recursive definition

# Data card or display block
class LCARSPanel(LCARSComponent):
    type: Literal["panel"]
    content: List["LCARSNode"]

# Specialized info block for log lines, alerts, messages
class LCARSLogEntry(LCARSComponent):
    type: Literal["log"]
    timestamp: Optional[str]
    severity: Optional[Literal["info", "warning", "error"]]
    message: str

# Tabbed container or selector
class LCARSTabs(LCARSComponent):
    type: Literal["tabs"]
    tabs: List[str]
    selected: Optional[str]
    panels: List["LCARSContainer"]

# Data table
class LCARSTable(LCARSComponent):
    type: Literal["table"]
    headers: List[str]
    rows: List[List[str]]

# Top-level view/page
class LCARSPage(TypedDict):
    id: str
    title: Optional[str]
    components: List[LCARSComponent]  # this can be any of LCARSText, LCARSButton, LCARSContainer, LCARSPanel, LCARSLogEntry, LCARSTabs, LCARSTable



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


def extract_markdown_block(text: str, type: str) -> str:
    if '```' not in text:
        print(f"extract_markdown_block: no ``` found in: {text}")
        return text
    if f"```{type}" in text:
        print(f"extract_markdown_block: found ```{type} in: {text}")
        return text.split(f"```{type}", 1)[1].split("```")[0]
    print(f"extract_markdown_block: found ``` but not ```{type} in: {text}")
    return text.split("```", 1)[1].split("```")[0]


def json_to_lcars_node(json_data: any, llm: any) -> LCARSPage:
    """Convert a JSON object into an LCARS node structure using LLM."""
    
    prompt = f"""
    Convert this JSON data into an LCARS UI structure:
    {json.dumps(json_data, indent=2)}
    
    Create an intuitive and user-friendly LCARS interface that represents this data.
    Consider grouping related information and creating a clear visual hierarchy.
    """
    
    return llm.with_structured_output(LCARSPage).invoke(prompt)


def json_to_lcars_html(json_data: any, llm: any) -> str:
    """Convert a JSON object into an LCARS HTML structure using LLM."""
    
    prompt = f"""
    Convert this JSON data into an LCARS HTML structure:
    {json.dumps(json_data, indent=2)}
    
    Create an intuitive and user-friendly LCARS interface that represents this data.
    Consider grouping related information and creating a clear visual hierarchy.

    The response must be a valid HTML document. There should be no buttons or interactive elements.
    The HTML should have css styles to make it look like a LCARS interface from the Star Trek The Next Generation.
    Don't include any javascript. Use inline css only. Provide only the content of the <body> tag.
    """
    
    res = llm.invoke(prompt).content
    return extract_markdown_block(res, "html")


def json_to_lcars_jsx(json_data: any, llm: any) -> str:
    prompt = f"""
Generate a JSX template to render the following JSON data:

```json
{json.dumps(json_data, indent=2)}
```

Only return the JSX template. Do not include the React component or javascript. Just the JSX template.
Do not include any <script> or <style> tags. 
Assume the the JSON is passed as a paramter called `props`. For example, if you have {{ "name": "Joe" }}, you should use `props.name` in the JSX template.
Consider using cards, flexboxes, tables, lists, and other css properties to make it look really cool.

Use inline styles to make the UI look like a LCARS interface from the Star Trek The Next Generation. 
Always render groups of numbers as progress bars and gauges.
Try to include all of the information from the JSON in the JSX template. We don't want to lose information.
Never use `JSON.stringify` in the JSX template. Do not use `JSON.stringify`. Don't use `JSON.stringify`.
"""
    # Use inline styles to make the UI look very classy and modern. 
    jsx_template = None
    for i in range(20):
        res = llm.invoke(prompt).content
        if '<style' in res:
            print('llm gave us a style tag, skipping')
            continue
        if 'JSON.stringify' in res:
            print('llm gave us a JSON.stringify, skipping')
            continue
        try:
            jsx_template = extract_markdown_block(res, "jsx")
            if jsx_template:
                break
        except:
            pass
    if jsx_template:
        # If jsx_template contains a function component definition, extract just the JSX template
        if "function" in jsx_template and "return" in jsx_template:
            try:
                # Find the JSX between return and the closing brace
                start = jsx_template.find("return") + 6  # Skip "return"
                end = jsx_template.rfind("}")
                if start > 6 and end > start:
                    jsx_template = jsx_template[start:end].strip()
            except:
                pass
        
        # Remove trailing ");", if present
        jsx_template = jsx_template.rstrip()
        if jsx_template.endswith(");"):
            jsx_template = jsx_template[:-2].rstrip()
        # Remove leading whitespace and opening parenthesis if present
        jsx_template = jsx_template.lstrip()
        if jsx_template.startswith('('):
            jsx_template = jsx_template[1:].lstrip()
        return jsx_template
    raise Exception("Failed to generate valid JSX")


def random_json(llm: any) -> any:
    prompt = """
Generate a JSON object based on an arbitrary topic.
Make it themed on Star Trek The Next Generation.
"""
    for i in range(10):
        print(f"Generating JSON {i}")
        res = llm.invoke(prompt).content
        try:
            jtext = extract_markdown_block(res, "json")
            print("text: ", jtext)
            j = json.loads(jtext)
            print(f"Generated JSON successfully{i}")
            return j
        except Exception as e:
            print(f"Failed to generate valid JSON {i}: {e}")
            pass
    raise Exception("Failed to generate valid JSON")


def reorganize_json(json_data: any, llm: any) -> any:
    prompt = f"""
Reorganize the following JSON data into a more logical structure. 
If the JSON is long, reorganize it to shorten it. 

```json
{json.dumps(json_data, indent=2)}
```

Respond with the JSON data only. Do not include any other text. Do not explain your response.
"""
    res = llm.invoke(prompt).content
    res = extract_markdown_block(res, "json")
    print(res)
    return json.loads(res)

if __name__ == "__main__":
    # Example usage:
    # lcars_structure = json_to_lcars_node(some_json, llm)
    # n = json_to_lcars_node(some_json, model)

    # print(json.dumps(n, indent=2))

    html = json_to_lcars_html(some_json, model)
    print(html)

