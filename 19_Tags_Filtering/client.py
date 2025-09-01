import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def list_with_tags(client):
    tools = await client.list_tools()
    rows = []
    for t in tools:
        tags = []
        if getattr(t, "meta", None):
            fm = t.meta.get("_fastmcp", {})
            if isinstance(fm, dict):
                tags = fm.get("tags", [])
        rows.append((t.name, tags))
    return rows

async def main():
    c = Client(StreamableHttpTransport("http://127.0.0.1:8020/mcp/"))
    async with c:
        # definiere Startzustand explizit
        await c.call_tool("set_mode", {"mode": "public"})
        print("public:", await list_with_tags(c))

        await c.call_tool("set_mode", {"mode": "admin"})
        print("admin:", await list_with_tags(c))
        res = await c.call_tool("do_top_secret_stuff", {})
        print("admin call:", res.data)

        await c.call_tool("set_mode", {"mode": "public"})
        res = await c.call_tool("add", {"a": 2, "b": 3})
        print("add(public):", res.data)

if __name__ == "__main__":
    asyncio.run(main())
