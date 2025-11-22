import asyncio
from mcp.server.fastmcp import FastMCP

# Initialize Server
mcp = FastMCP("VulnerabilityServer")

# Mock Data
CVE_DB = {
    "CVE-2024-0001": "Critical: Remote Code Execution in Login Service. CVSS 9.8.",
    "CVE-2024-0002": "Medium: Cross-Site Scripting in Dashboard. CVSS 5.4.",
    "CVE-2024-0003": "Low: Information Disclosure in API. CVSS 3.1."
}

@mcp.tool()
def get_cve_details(cve_id: str) -> str:
    """
    Get details for a specific Common Vulnerabilities and Exposures (CVE) ID.
    Args:
        cve_id: The ID of the vulnerability (e.g., CVE-2024-0001)
    """
    return CVE_DB.get(cve_id, "CVE not found in database.")

@mcp.tool()
def list_recent_cves() -> str:
    """List all known CVEs in the database."""
    return ", ".join(CVE_DB.keys())

if __name__ == "__main__":
    print("### Lab 5.1: MCP Server (Solution) ###")
    print("This script runs an MCP server over Stdio.")
    print("To test this, you would typically configure an MCP Client (like Claude Desktop) to run this script.")
    print("For now, we will just simulate a tool call locally.")
    
    # Simulate internal call
    print(f"\nQuerying CVE-2024-0001: {get_cve_details('CVE-2024-0001')}")
    
    # Uncomment to actually run the server
    # mcp.run()
