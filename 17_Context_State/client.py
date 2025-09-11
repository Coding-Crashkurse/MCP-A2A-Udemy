import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    client = Client(StreamableHttpTransport("http://127.0.0.1:8000/mcp/"))
    async with client:
        for i in range(3):
            res = await client.call_tool("increment_counter", {})
            print(f"Call {i+1}: counter = {res.data}")
        await client.call_tool("reset_counter", {})
        res = await client.call_tool("increment_counter", {})
        print(f"After reset: counter = {res.data}")

if __name__ == "__main__":
    asyncio.run(main())
