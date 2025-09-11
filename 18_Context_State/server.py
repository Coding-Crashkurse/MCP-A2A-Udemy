from fastmcp import FastMCP, Context

mcp = FastMCP(
    name="ContextStateServer",
    stateless_http=False,
)

@mcp.tool(description="Increment session counter and return new value.")
def increment_counter(ctx: Context) -> int:
    current = ctx.get_state("counter") or 0
    new_val = int(current) + 1
    ctx.set_state("counter", new_val)
    return new_val

@mcp.tool(description="Reset session counter to zero.")
def reset_counter(ctx: Context) -> int:
    ctx.set_state("counter", 0)
    return 0

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1")
