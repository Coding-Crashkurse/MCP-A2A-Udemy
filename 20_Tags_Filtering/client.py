import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    c1 = Client(StreamableHttpTransport("http://localhost:8000/mcp/?tags=math"))
    async with c1:
        tools = await c1.list_tools()
        print("http://localhost:8000/mcp/?tags=math")
        print("COUNT:", len(tools))
        for t in tools:
            print(t.name)

    c2 = Client(StreamableHttpTransport("http://localhost:8000/mcp/?tags=search"))
    async with c2:
        tools = await c2.list_tools()
        print("http://localhost:8000/mcp/?tags=search")
        print("COUNT:", len(tools))
        for t in tools:
            print(t.name)

if __name__ == "__main__":
    asyncio.run(main())
