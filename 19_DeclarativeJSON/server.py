from fastmcp import FastMCP

mcp = FastMCP(name="DeclarativeJSONDemo")

@mcp.tool(description="Add two integers")
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(description="Simple health/ping")
def ping() -> str:
    return "pong"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8018, path="/mcp/")
