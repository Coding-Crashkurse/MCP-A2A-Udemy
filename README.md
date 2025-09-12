## Model Context Protocol (MCP) Course Directory Overview
This document gives you a chapter-by-chapter map of the MCP-A2A Udemy repository. Each folder focuses on one key concept or tool in the Model Context Protocol ecosystem.

---

# Directories

## 01_FirstMCPServer 💡
Setting up and running your first basic server that implements the Model Context Protocol.

## 02_TransportMethods
Exploring different transport methods: `SSE` (Server-Sent Events), `streamable-http` (stateless vs. stateful), and `stdio` for MCP communication.

## 03_RessourcesPromptsTools
Defining and managing resources, prompts, and tools within the MCP framework.

## 04_Context
Deep dive into the powerful `Context` object of the FastMCP package.

## 05_Discovery
Dynamically updating clients when a server adds, updates, or removes tools.

## 06_Roots
Understanding roots in MCP: boundaries that tell servers where they may operate and how clients can announce relevant resources.

## 07_Sampling
Letting servers request LLM completions through the client. Techniques for sampling context, selecting tools, and managing information flow.

## 08_LangGraph_MCP
Integrating MCP with LangGraph to connect an MCP Server to a modern LLM.

## 09_Authorization
Securing MCP services through proper authorization mechanisms. This chapter demonstrates how to implement the OAuth 2.1 workflow using Auth0 as the identity provider.

## 10_Fastapi_Integration
Embedding MCP servers into the FastAPI ecosystem to create robust, production-ready services.

## 11_Composition
Strategies for composing multiple, independent MCP services into one cohesive system.

## 12_Proxy_Servers
Proxies that bridge legacy SSE traffic to the new streamable-http method, while routing and enhancing requests.

## 13_Capstone
A full-stack, Docker-based AI web application (frontend + API server + MCP server) that ties together everything you’ve learned.

## 14_Env_ToolFlags
Env-driven tool enabling with `.env` flags (`MCP_TOOL_ADD`, `MCP_TOOL_SUBTRACT`). The client lists tools over HTTP. Focus: feature toggles without middleware or tags.

## 15_StructuredOutputs
Structured tool outputs using MCP output schemas (2025-06-18) in FastMCP >= 2.10.0. Returns a `CallToolResult` with auto-deserialized JSON.

## 16_Elicitation
Elicitation per the 2025-06-18 MCP update in FastMCP >= 2.10.0. The server requests extra input and the client supplies it, including implicit and no-response flows.

## 17_Middleware
Intercepts `list_tools` and `call_tool` with MCP middleware for auth, logging, rate limiting, and error handling introduced in 2.9.0.

## 18_Context_State
Uses `Context.session_id` for per-session state plus `report_progress` and logging. Compatible with FastMCP >=2.9.x

## 19_DeclarativeJSON
Declarative server configuration via `fastmcp.json`. Uses the MCP-JSON CLI export added in 2.10.3.

## 20_Tags_Filtering
Filters tools by query `?tags=...` in a `list_tools` middleware against `component.tags`.

---

Happy Coding! 🎉