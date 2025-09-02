# client.py
import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

URL_MATH          = "http://127.0.0.1:8052/mcp/?tags=math"
URL_SEARCH        = "http://127.0.0.1:8052/mcp/?tags=search"
URL_BOTH_REPEAT   = "http://127.0.0.1:8052/mcp/?tags=math&tags=search"
URL_BOTH_COMMA    = "http://127.0.0.1:8052/mcp/?tags=math,search"

async def show(url: str):
    c = Client(StreamableHttpTransport(url))
    async with c:
        tools = await c.list_tools()
        print(url, "->", [t.name for t in tools])

async def main():
    await show(URL_MATH)
    await show(URL_SEARCH)
    await show(URL_BOTH_REPEAT)
    await show(URL_BOTH_COMMA)

if __name__ == "__main__":
    asyncio.run(main())
