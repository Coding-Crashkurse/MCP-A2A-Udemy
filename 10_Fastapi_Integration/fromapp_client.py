import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

SERVER = "http://127.0.0.1:3000/mcp/"


def section(title: str):
    print(f"\n{'=' * 10} {title} {'=' * 10}")


async def main() -> None:
    async with Client(StreamableHttpTransport(SERVER)) as session:
        resources = await session.list_resources()
        section("Available Resources")
        for res in resources:
            print(f"Resource Name: {res.name}    URI: {res.uri}")

        list_uri = str(resources[0].uri)

        tools = await session.list_tools()
        section("Available Tools")
        for tool in tools:
            print(f"Tool Name: {tool.name}")

        all_products = await session.read_resource(list_uri)
        section("All Products (Before)")
        print(all_products[0].text)

        create_tool_name = tools[0].name

        section(f"Calling Tool: {create_tool_name}")
        created = await session.call_tool(
            create_tool_name,
            {"name": "Widget", "price": 19.99},
        )
        # pre-v2.10: result was a list of Content objects
        # print("Created product:", created[0].text)
        # v2.10+: result is a single CallToolResult object
        print("Created product:", created.data)

        updated_products = await session.read_resource(list_uri)
        section("All Products (After)")
        print(updated_products[0].text)


if __name__ == "__main__":
    asyncio.run(main())
