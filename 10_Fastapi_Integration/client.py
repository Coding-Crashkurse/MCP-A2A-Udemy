import asyncio

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport


async def main():
    transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcpserver/mcp")
    client = Client(transport=transport)

    async with client:
        result = await client.call_tool("add", {"a": 5, "b": 7})
        # pre-v2.10: result was a list of Content objects, so we accessed the first item.
        # print("5 + 7 =", result[0].text)
        
        # v2.10+: result is a single CallToolResult object.
        print("5 + 7 =", result.data)


if __name__ == "__main__":
    asyncio.run(main())