from fastmcp import FastMCP, Context

mcp = FastMCP(
    name="ContextStateServer",
    stateless_http=False,  # nötig für ctx.state
)

@mcp.tool(description="Increment session counter and return new value.")
def increment_counter(ctx: Context) -> int:
    v = ctx.state.get("counter", 0) + 1
    ctx.state["counter"] = v
    return v

@mcp.tool(description="Reset session counter to zero.")
def reset_counter(ctx: Context) -> int:
    ctx.state["counter"] = 0
    return 0

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8016, path="/mcp/")
