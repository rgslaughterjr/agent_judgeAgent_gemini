import asyncio
# pip install mcp
from mcp.server.fastmcp import FastMCP

# Initialize Server
mcp = FastMCP("VulnerabilityServer")

# --- Step 1: Define Tool ---
@mcp.tool()
def get_cve_details(cve_id: str) -> str:
    """
    TODO: Return details for a given CVE ID.
    """
    # Mock database
    # if cve_id == "CVE-2024-0001": return "Critical SQL Injection..."
    return "Unknown CVE"

def run_lab_5_1():
    print("### Lab 5.1: MCP Server ###")
    print("Starting MCP Server on Stdio...")
    # mcp.run() 

if __name__ == "__main__":
    run_lab_5_1()
