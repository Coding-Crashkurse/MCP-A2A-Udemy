import asyncio

import mcp.types as types
from fastmcp import Client
from fastmcp.client.logging import LogMessage
from fastmcp.client.transports import StreamableHttpTransport


async def message_handler(msg):
    if not isinstance(msg, types.ServerNotification):
        return

    root = msg.root
    if isinstance(root, types.ProgressNotification):
        p = root.params
        print(f"[Progress] {p.progress}/{p.total or '?'}")


async def log_handler(params: LogMessage):
    level = params.level.upper()
    print(f"[Log – {level}] {params.data}")


async def main():
    transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp")
    client = Client(transport, message_handler=message_handler, log_handler=log_handler)

    async with client:
        tools = await client.list_tools()
        print("→ Available tools:", [t.name for t in tools])

        print("→ Calling process_items…")
        items = ["one", "two", "three", "four", "five"]
        result = await client.call_tool("process_items", {"items": items})
        print("RESULT", result)

        # pre-v2.10: result was a list of Content objects, requiring a list comprehension.
        # processed = [c.text for c in result]
        
        # v2.10+: result is a single CallToolResult object.
        processed = result.data
        print("→ Result:", processed)


if __name__ == "__main__":
    asyncio.run(main())