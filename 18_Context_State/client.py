import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    client = Client(StreamableHttpTransport(url="http://127.0.0.1:8000/mcp/"))
    async with client:
        tools = await client.list_tools()
        print("TOOLS:", [t.name for t in tools])

        r1 = await client.call_tool("create_note", {"text": "hello"})
        print("CREATE:", r1.data)

        r2 = await client.call_tool("list_notes", {})
        print("LIST:", r2.data)

if __name__ == "__main__":
    asyncio.run(main())
