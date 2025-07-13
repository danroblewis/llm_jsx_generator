from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from typing import TypedDict
import json



model = ChatOpenAI(
    base_url="https://498916909b03.ngrok-free.app/v1",
    model="llama3.2:3b",
    temperature=0.7,
    max_tokens=1000,
    max_retries=3,
    timeout=1000,
)

class Yuppie(TypedDict):
    name: str
    age: int
    occupation: str 

res = model.with_structured_output(Yuppie).invoke("Hello, world! he works at google")
print(res)





