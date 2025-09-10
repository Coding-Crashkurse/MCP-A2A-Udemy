import os
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

mcp = FastMCP(name="SimpleDemo")

@mcp.tool(enabled=os.getenv("MCP_TOOL_ADD") == "True")
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(enabled=os.getenv("MCP_TOOL_SUBTRACT") == "True")
def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1")
