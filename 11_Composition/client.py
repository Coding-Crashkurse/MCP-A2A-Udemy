import asyncio

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport


async def main():
    transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp/")
    client = Client(transport=transport)

    async with client:
        tools = await client.list_tools()
        print("=== Available Tools ===")
        for tool in tools:
            print(f"Tool Name: {tool.name}")
        print()

        result_add = await client.call_tool("add_add", {"a": 5, "b": 7})
        # pre-v2.10: result was a list of Content objects, so we accessed the first item.
        # print("5 + 7 =", result_add[0].text)
        
        # v2.10+: result is a single CallToolResult object.
        print("5 + 7 =", result_add.data)

        result_subtract = await client.call_tool("subtract_subtract", {"a": 10, "b": 3})
        # pre-v2.10: result was a list of Content objects, so we accessed the first item.
        # print("10 - 3 =", result_subtract[0].text)
        
        # v2.10+: result is a single CallToolResult object.
        print("10 - 3 =", result_subtract.data)


if __name__ == "__main__":
    asyncio.run(main())