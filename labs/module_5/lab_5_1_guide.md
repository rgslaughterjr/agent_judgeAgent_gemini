# Lab 5.1: Building a Vulnerability MCP Server

## Goal

Learn how to build a **Model Context Protocol (MCP)** server. MCP is a new standard that allows agents (like Claude or Gemini) to connect to external tools and data sources in a standardized way.

## Concepts

### 1. MCP Server

A server that exposes **Tools** and **Resources**.

* **Tools**: Functions the LLM can call (e.g., `query_cve(id="CVE-2024-1234")`).
* **Resources**: Data the LLM can read (e.g., `cve://list`).

### 2. FastMCP (Python)

We will use the `mcp` library (specifically the high-level `FastMCP` if available, or standard `Server` class) to define our server.

## Instructions

1. **Open `lab_5_1_starter.py`**.
2. **Step 1**: Initialize the MCP Server.
3. **Step 2**: Define a tool `get_cve_details(cve_id: str)` that returns mock data for a vulnerability.
4. **Step 3**: Run the server. (Note: MCP servers usually run over Stdio or SSE. For this lab, we will simulate a local run or use the stdio transport).

## Resources

* [Model Context Protocol Spec](https://modelcontextprotocol.io/)
