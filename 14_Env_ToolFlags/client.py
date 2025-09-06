import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    c = Client(StreamableHttpTransport("http://localhost:5050/"))
    async with c:
        tools = await c.list_tools()
        print("COUNT:", len(tools))
        for t in tools:
            print(t.name)

if __name__ == "__main__":
    asyncio.run(main())
