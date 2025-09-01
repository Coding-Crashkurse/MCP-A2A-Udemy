from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware, MiddlewareContext

mcp = FastMCP(name="TagServerWithFilterMW")

@mcp.tool(meta={"tags": ["public"]}, description="Add for public")
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(meta={"tags": ["admin"]}, description="Do top secret stuff")
def do_top_secret_stuff() -> str:
    return "classified operation complete"

class TagFilteringMiddleware(Middleware):
    async def on_list_tools(self, context: MiddlewareContext, call_next):
        result = await call_next(context)
        qp = context.fastmcp_context.request_context.request.query_params
        tags = qp.getlist("tags")
        if not tags:
            return result
        if len(tags) == 1 and "," in tags[0]:
            tags = {t.strip() for t in tags[0].split(",") if t.strip()}
        else:
            tags = set(tags)
        return [tool for tool in result if getattr(tool, "tags", set()) & tags]

mcp.add_middleware(TagFilteringMiddleware())

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8021, path="/mcp/")
