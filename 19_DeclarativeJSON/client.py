import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    client = Client(StreamableHttpTransport("http://127.0.0.1:8018/mcp/"))
    async with client:
        res = await client.call_tool("add", {"a": 2, "b": 3})
        print("add:", res.data)

if __name__ == "__main__":
    asyncio.run(main())
