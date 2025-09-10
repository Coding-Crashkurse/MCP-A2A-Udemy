import asyncio
from fastmcp import Client
from fastmcp.client.elicitation import ElicitRequestParams
from fastmcp.client.transports import StreamableHttpTransport

async def elicitation_handler(message: str, response_type: type | None, params: ElicitRequestParams, context) -> dict:
    print(f"\n[Server]: {message}")
    ans = input("Antwort (yes/no): ").strip()
    return {"value": ans}

async def main():
    client = Client(StreamableHttpTransport(url="http://127.0.0.1:8000/mcp/"), elicitation_handler=elicitation_handler)
    async with client:
        res = await client.call_tool("add_with_confirmation", {"a": 10, "b": 5})
        print("Result:", res.data)

if __name__ == "__main__":
    asyncio.run(main())
