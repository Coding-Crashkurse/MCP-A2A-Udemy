from fastmcp import FastMCP, Context
from fastmcp.server.elicitation import AcceptedElicitation

mcp = FastMCP(name="ElicitationServer")

@mcp.tool(description="Add two integers after explicit confirmation.")
async def add_with_confirmation(a: int, b: int, ctx: Context) -> int:
    resp = await ctx.elicit(message=f"Type 'yes' to add {a} and {b}.", response_type=str)
    if isinstance(resp, AcceptedElicitation):
        await ctx.info("Confirmed by user.")
        return a + b
    await ctx.info("Declined by user.")
    return 0

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1")
