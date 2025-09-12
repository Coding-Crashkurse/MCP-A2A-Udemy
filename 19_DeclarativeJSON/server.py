from fastmcp import FastMCP

mcp = FastMCP(name="DeclarativeJSONDemo")

@mcp.tool(description="Add two integers")
def add(a: int, b: int) -> int:
    return a + b