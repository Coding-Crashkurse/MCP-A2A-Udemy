import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    client = Client(StreamableHttpTransport("http://127.0.0.1:8000/mcp/"))
    async with client:
        res = await client.call_tool("add", {"a": 21, "b": 21})
        print("Result:", res.data)
        # print(f"{res.data.input_a} + {res.data.input_b} = {res.data.result}")

if __name__ == "__main__":
    asyncio.run(main())
