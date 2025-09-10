import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    client = Client(StreamableHttpTransport(url="http://127.0.0.1:8000/mcp/"))
    async with client:
        available_tools = await client.list_tools()
        print("COUNT:", len(available_tools))
        for tool in available_tools:
            print(tool.name)

if __name__ == "__main__":
    asyncio.run(main())
