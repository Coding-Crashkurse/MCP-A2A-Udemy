import asyncio

from dotenv import load_dotenv
from fastmcp import Client
from fastmcp.client.sampling import RequestContext, SamplingMessage, SamplingParams
from fastmcp.client.transports import StreamableHttpTransport
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()


async def sampling_handler(
    messages: list[SamplingMessage], params: SamplingParams, context: RequestContext
) -> str:
    print("[Client] sampling_handler invoked")
    print(f"[Client] Received {len(messages)} message(s), params: {params}")

    lc_msgs = []
    if params.systemPrompt:
        print("[Client] Using system_prompt:", params.systemPrompt)
        lc_msgs.append(SystemMessage(content=params.systemPrompt))

    for idx, msg in enumerate(messages, start=1):
        print(f"[Client] Message #{idx} content:", msg.content.text)
        lc_msgs.append(HumanMessage(content=msg.content.text))

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=params.temperature or 0.0,
        max_tokens=params.maxTokens or 64,
    )

    result = await llm.ainvoke(input=lc_msgs)
    return result.content


async def main():
    transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp/")
    client = Client(transport, sampling_handler=sampling_handler)

    # Example function code for which we want a docstring
    code_snippet = """\
def add(a: int, b: int) -> int:
    return a + b
"""

    async with client:
        result = await client.call_tool("generate_docstring", {"code": code_snippet})

        # pre-v2.10: result was a list of Content objects, so we accessed the first item.
        # print("Generated Docstring:\n", result[0].text)
        
        # v2.10+: result is a single CallToolResult object.
        print("Generated Docstring:\n", result.data)


if __name__ == "__main__":
    asyncio.run(main())