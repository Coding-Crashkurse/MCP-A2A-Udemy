import asyncio
from typing import Any

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

SERVER_URL = "http://127.0.0.1:8052/mcp/"

# ---------- helpers ----------
def _meta(obj: Any) -> dict:
    # Tools haben .meta; wir ignorieren _meta (Prompts), da nur Tools genutzt werden
    return getattr(obj, "meta", None) or {}

def _tags(obj: Any) -> list[str]:
    meta = _meta(obj)
    return (meta.get("_fastmcp", {}) or {}).get("tags", []) or []

def filter_tools_by_tag(tools, tag: str):
    return [t for t in tools if tag in _tags(t)]

def filter_tools_by_tags_any(tools, tags: set[str] | list[str]):
    tags = set(tags)
    return [t for t in tools if tags.intersection(_tags(t))]

def filter_tools_by_meta_eq(tools, key: str, value: Any):
    out = []
    for t in tools:
        m = _meta(t)
        # nur eigene Meta-Felder matchen, nicht _fastmcp
        if key in m and m[key] == value:
            out.append(t)
    return out

# ---------- main ----------
async def main():
    client = Client(StreamableHttpTransport(SERVER_URL))

    async with client:
        tools = await client.list_tools()
        for t in tools:
            print("NAME:", t.name)
            print("META:", getattr(t, "meta", None))
            tags = (getattr(t, "meta", {}) or {}).get("_fastmcp", {}).get("tags", [])
            print("TAGS:", tags)

if __name__ == "__main__":
    asyncio.run(main())
