from fastmcp import FastMCP

mcp = FastMCP(name="TagServerBasic")

@mcp.tool(meta={"tags": ["public"]}, description="Add for public")
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(meta={"tags": ["admin"]}, description="Do top secret stuff")
def do_top_secret_stuff() -> str:
    return "classified operation complete"

@mcp.tool(description="Switch visible set: public | admin")
def set_mode(mode: str = "public") -> dict:
    groups = {
        "public": [add],
        "admin":  [do_top_secret_stuff],
    }
    for t in {add, do_top_secret_stuff}:
        t.disable()
    for t in groups.get(mode, []):
        t.enable()
    return {"mode": mode, "enabled": [t.name for t in groups.get(mode, [])]}

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8020, path="/mcp/")
