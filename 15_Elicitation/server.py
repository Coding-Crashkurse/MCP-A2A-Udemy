import asyncio
from fastmcp import FastMCP, Context
from fastmcp.server.elicitation import AcceptedElicitation

mcp = FastMCP(name="ElicitationServer")

@mcp.tool(description="Add two integers after explicit confirmation.")
async def add_with_confirmation(a: int, b: int, ctx: Context) -> int:
    prompt = f"Are you sure you want to add {a} and {b}? (yes/no)"
    resp = await ctx.elicit(message=prompt, response_type=str)

    if isinstance(resp, AcceptedElicitation) and str(resp.data).strip().lower() in {"yes", "y"}:
        await ctx.info("Confirmed by user.")
        return a + b
    await ctx.info("Cancelled by user.")
    return 0

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8015, path="/mcp/")
