# fromapp_client_208.py
import asyncio
import json
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

SERVER = "http://127.0.0.1:3000/mcp/"


def section(title: str):
    print(f"\n{'=' * 10} {title} {'=' * 10}")


async def main() -> None:
    async with Client(StreamableHttpTransport(SERVER)) as session:
        tools = await session.list_tools()
        section("Available Tools")
        for tool in tools:
            print(f"Tool Name: {tool.name}")

        list_products_tool_name = "list_products_products_get"
        create_product_tool_name = "create_product_products_post"

        list_products_result = await session.call_tool(list_products_tool_name)
        section("All Products (Before)")
        # v2.10+: call_tool returns a CallToolResult; use `.data`

        section(f"Calling Tool: {create_product_tool_name}")
        created_result = await session.call_tool(
            create_product_tool_name,
            {"name": "Widget", "price": 19.99},
        )
        # v2.10+: CallToolResult payload is in `.data`
        print("Created product:", created_result.data)

        updated_products_result = await session.call_tool(list_products_tool_name, {})
        section("All Products (After)")
        # v2.10+: CallToolResult → `.data`
        print(json.dumps(updated_products_result.data, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
