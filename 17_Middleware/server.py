import time
from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware

mcp = FastMCP(name="MiddlewareServer")

class TimingMiddleware(Middleware):
    async def __call__(self, call, nxt):
        t0 = time.perf_counter()
        resp = await nxt(call)
        dt_ms = (time.perf_counter() - t0) * 1000.0
        print(f"[middleware] {call.tool_name} took {dt_ms:.2f} ms")
        return resp

mcp.add_middleware(TimingMiddleware())

@mcp.tool(description="Add two integers")
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8017, path="/mcp/")
