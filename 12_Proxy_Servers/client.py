import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

PROXY_URL = "http://127.0.0.1:8000/mcp/"

async def main():
    print(f"Connecting to proxy at {PROXY_URL}")
    client = Client(transport=StreamableHttpTransport(url=PROXY_URL))

    async with client:
        print("Calling add")
        res_add = await client.call_tool("add_add", {"a": 7, "b": 5})
        if res_add:
            # pre-v2.10: result was a list of Content objects, so we accessed the first item.
            # print(f"add response: {res_add[0].text}")

            # v2.10+: result is a single CallToolResult object.
            print(f"add response: {res_add.data}")

        print("Calling subtract")
        res_sub = await client.call_tool("subtract_subtract", {"a": 7, "b": 5})
        if res_sub:
            # pre-v2.10: result was a list of Content objects, so we accessed the first item.
            # print(f"subtract response: {res_sub[0].text}")
            
            # v2.10+: result is a single CallToolResult object.
            print(f"subtract response: {res_sub.data}")

if __name__ == "__main__":
    asyncio.run(main())