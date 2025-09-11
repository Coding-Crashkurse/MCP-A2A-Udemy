from collections import defaultdict
from fastmcp import FastMCP, Context
from fastmcp.server.middleware import Middleware, MiddlewareContext

mcp = FastMCP(name="ContextStateDemo")
NOTES = defaultdict(list)

class AuthMiddleware(Middleware):
    async def on_call_tool(self, context: MiddlewareContext, call_next):
        context.fastmcp_context.set_state("current_user", {"name": "Admin"})
        return await call_next()

mcp.add_middleware(AuthMiddleware())

@mcp.tool
def create_note(text: str, ctx: Context) -> dict:
    user = ctx.get_state("current_user") or {}
    name = user.get("name", "anonymous")
    if name == "Admin":
        return {"ok": False, "error": "Admin ist read-only"}
    NOTES[name].append(text)
    return {"ok": True, "note": text, "total": len(NOTES[name])}

@mcp.tool
def list_notes(ctx: Context) -> dict:
    user = ctx.get_state("current_user") or {}
    name = user.get("name", "anonymous")
    return {"ok": True, "user": name, "notes": list(NOTES.get(name, []))}

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
