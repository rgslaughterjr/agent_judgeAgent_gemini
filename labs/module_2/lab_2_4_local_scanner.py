import json
import os
from pathlib import Path
from typing import List, Dict
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Reuse the ComplianceReport from Lab 2.1
class ComplianceReport(BaseModel):
    """Structured compliance assessment report"""
    policy_name: str = Field(description="The security policy or framework being assessed against")
    system_name: str = Field(description="Name of the system being analyzed")
    compliant: bool = Field(description="Overall compliance status")
    confidence_score: float = Field(description="Confidence in assessment (0.0 to 1.0)")
    critical_findings: List[str] = Field(description="Critical security issues requiring immediate action")
    high_findings: List[str] = Field(description="High priority security issues")
    medium_findings: List[str] = Field(description="Medium priority security issues")
    low_findings: List[str] = Field(description="Low priority or informational findings")
    recommendations: List[str] = Field(description="Specific remediation recommendations")

def load_target_system(filename: str) -> Dict:
    """Load a target system configuration from JSON"""
    target_dir = Path("data/target_systems")
    filepath = target_dir / filename
    
    if not filepath.exists():
        raise FileNotFoundError(f"System config not found: {filepath}")
    
    with open(filepath, 'r') as f:
        return json.load(f)

def format_system_for_analysis(system_config: Dict) -> str:
    """Convert JSON config to readable text for LLM analysis"""
    lines = []
    lines.append(f"System: {system_config.get('system_name', 'Unknown')}")
    lines.append(f"Environment: {system_config.get('environment', 'Unknown')}")
    lines.append(f"Owner: {system_config.get('owner', 'Unknown')}")
    lines.append(f"Last Audit: {system_config.get('last_audit', 'Never')}")
    lines.append(f"Compliance Frameworks: {', '.join(system_config.get('compliance_frameworks', []))}")
    lines.append("\nSecurity Controls:")
    
    # Format security controls
    controls = system_config.get('security_controls', {})
    for category, settings in controls.items():
        lines.append(f"\n{category.upper().replace('_', ' ')}:")
        lines.append(json.dumps(settings, indent=2))
    
    # Add known issues if present
    if 'known_issues' in system_config:
        lines.append("\nKnown Issues:")
        for issue in system_config['known_issues']:
            lines.append(f"  - {issue}")
    
    return "\n".join(lines)

def analyze_system(system_filename: str, policy_name: str = "Security Baseline") -> ComplianceReport:
    """
    Analyze a target system against security policies
    
    Args:
        system_filename: Name of JSON file in data/target_systems/
        policy_name: Name of the policy framework to assess against
        
    Returns:
        ComplianceReport with structured findings
    """
    print(f"\n{'='*70}")
    print(f"Analyzing: {system_filename}")
    print(f"{'='*70}\n")
    
    # Load system configuration
    system_config = load_target_system(system_filename)
    system_description = format_system_for_analysis(system_config)
    
    # Define security policy (you can load this from a file too)
    security_policy = """
    SECURITY BASELINE REQUIREMENTS:
    
    1. ENCRYPTION:
       - All data at rest must use AES-256 encryption
       - All data in transit must use TLS 1.2 or higher
       - Encryption keys must rotate every 90 days
       - Key management must use a secure vault (KMS, HashiCorp Vault, etc.)
    
    2. AUTHENTICATION:
       - Multi-factor authentication (MFA) must be enforced for all users
       - Passwords must be at least 12 characters with high complexity
       - Password rotation every 90 days
       - Session timeout must be 30 minutes or less
    
    3. NETWORK SECURITY:
       - Firewall must be enabled
       - Only necessary ports should be exposed
       - SSH access must use key-based authentication only
       - SSH must be restricted to specific IP ranges (no 0.0.0.0/0)
    
    4. LOGGING & MONITORING:
       - Centralized logging must be enabled
       - Logs must be retained for at least 90 days
       - SIEM integration required for production systems
       - Real-time alerting must be configured
       - Audit trails must be maintained
    
    5. ACCESS CONTROL:
       - Role-Based Access Control (RBAC) must be implemented
       - Least privilege principle must be enforced
       - Privileged access must be managed separately
       - Access reviews must occur quarterly
    
    6. VULNERABILITY MANAGEMENT:
       - Automated vulnerability scanning must run at least weekly
       - Critical patches must be applied within 48 hours
       - High patches must be applied within 7 days
    
    7. DATA PROTECTION:
       - Backups must be enabled and encrypted
       - Backup frequency must be at least daily
       - Disaster recovery must be tested annually
       - RTO must be 8 hours or less
       - RPO must be 4 hours or less
    """
    
    # Create LLM chain with structured output
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    structured_llm = llm.with_structured_output(ComplianceReport)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a senior security auditor conducting a compliance assessment.

Analyze the system configuration against the security policy requirements.
Categorize findings by severity: CRITICAL, HIGH, MEDIUM, LOW.

CRITICAL: Immediate security risk, data exposure, or compliance violation
HIGH: Significant security gap that should be addressed urgently  
MEDIUM: Security improvement needed but not urgent
LOW: Best practice recommendation or minor issue

Be thorough and specific. For each finding, explain what's wrong and why it matters."""),
        ("user", """Security Policy:
{policy}

System Configuration:
{system}

Provide a detailed compliance assessment.""")
    ])
    
    chain = prompt | structured_llm
    
    # Run analysis
    result = chain.invoke({
        "policy": security_policy,
        "system": system_description
    })
    
    # Display results
    print(f"System: {result.system_name}")
    print(f"Policy: {result.policy_name}")
    print(f"Compliant: {'✅ YES' if result.compliant else '❌ NO'}")
    print(f"Confidence: {result.confidence_score:.1%}")
    
    if result.critical_findings:
        print(f"\n🚨 CRITICAL FINDINGS ({len(result.critical_findings)}):")
        for i, finding in enumerate(result.critical_findings, 1):
            print(f"  {i}. {finding}")
    
    if result.high_findings:
        print(f"\n⚠️  HIGH FINDINGS ({len(result.high_findings)}):")
        for i, finding in enumerate(result.high_findings, 1):
            print(f"  {i}. {finding}")
    
    if result.medium_findings:
        print(f"\n📋 MEDIUM FINDINGS ({len(result.medium_findings)}):")
        for i, finding in enumerate(result.medium_findings, 1):
            print(f"  {i}. {finding}")
    
    if result.low_findings:
        print(f"\n💡 LOW/INFO FINDINGS ({len(result.low_findings)}):")
        for i, finding in enumerate(result.low_findings, 1):
            print(f"  {i}. {finding}")
    
    if result.recommendations:
        print(f"\n✅ RECOMMENDATIONS ({len(result.recommendations)}):")
        for i, rec in enumerate(result.recommendations, 1):
            print(f"  {i}. {rec}")
    
    return result

def scan_all_systems():
    """Scan all systems in the target_systems directory"""
    target_dir = Path("data/target_systems")
    json_files = list(target_dir.glob("*.json"))
    
    print(f"\n{'='*70}")
    print(f"SCANNING {len(json_files)} SYSTEMS")
    print(f"{'='*70}")
    
    results = []
    for json_file in json_files:
        result = analyze_system(json_file.name)
        results.append(result)
        print("\n")
    
    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    compliant_count = sum(1 for r in results if r.compliant)
    print(f"Total Systems: {len(results)}")
    print(f"Compliant: {compliant_count}")
    print(f"Non-Compliant: {len(results) - compliant_count}")
    
    return results

if __name__ == "__main__":
    print("=== Lab 2.4: Local System Scanner ===\n")
    
    # Option 1: Scan a specific system
    # result = analyze_system("api_vulnerable.json")
    
    # Option 2: Scan all systems
    results = scan_all_systems()
