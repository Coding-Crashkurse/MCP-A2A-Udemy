from fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP(name="StructuredOutputServer")

class AddResult(BaseModel):
    input_a: int = Field(description="First operand")
    input_b: int = Field(description="Second operand")
    result: int = Field(description="Sum")

@mcp.tool(description="Add two integers and return a structured result.")
def add(a: int, b: int) -> AddResult:
    return AddResult(input_a=a, input_b=b, result=a + b)

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1")
