from typing import List
from pydantic import BaseModel, Field, field_validator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Step 1: Define the Schema ---
class ComplianceReport(BaseModel):
    """
    Structured output for compliance analysis.
    
    This ensures the LLM returns validated JSON instead of free text.
    """
    policy_name: str = Field(
        description="The name or identifier of the policy being analyzed"
    )
    
    compliant: bool = Field(
        description="Whether the system is compliant with the policy (true/false)"
    )
    
    confidence_score: float = Field(
        description="Confidence level of the assessment, between 0.0 (no confidence) and 1.0 (high confidence)"
    )
    
    missing_controls: List[str] = Field(
        description="List of security controls or requirements that are missing or not implemented"
    )

    # --- Step 2: Add Validators ---
    @field_validator('confidence_score')
    @classmethod
    def check_score(cls, v):
        """
        Validate that confidence_score is between 0 and 1.
        
        This prevents the LLM from returning invalid values like 5.0 or -0.3
        """
        if v < 0 or v > 1:
            raise ValueError("Confidence score must be between 0.0 and 1.0")
        return v
    
    @field_validator('policy_name')
    @classmethod
    def check_policy_name(cls, v):
        """Ensure policy name is not empty"""
        if not v or v.strip() == "":
            raise ValueError("Policy name cannot be empty")
        return v.strip()

def run_lab_2_1():
    print("=== Lab 2.1: Pydantic Validators for Compliance ===\n")
    
    # Sample Input: A policy and an observed system
    policy_text = """
    The system must encrypt all data at rest using AES-256.
    Multi-factor authentication is required for all admin access.
    """
    
    observed_system = """
    The database is encrypted with AES-256.
    Admin access uses a simple password.
    """

    print("Policy Requirements:")
    print(policy_text)
    print("\nObserved System:")
    print(observed_system)
    print("\n" + "="*60)

    # --- Step 3: Create Chain with Structured Output ---
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # Bind the Pydantic schema to the LLM
    # This forces the LLM to return JSON matching ComplianceReport
    structured_llm = llm.with_structured_output(ComplianceReport)

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a strict compliance auditor. 
        
Analyze the observed system against the policy requirements.
Return a structured compliance report with:
- Whether the system is compliant (true/false)
- Your confidence in this assessment (0.0 to 1.0)
- List of missing controls or requirements

Be thorough and specific about what's missing."""),
        ("user", "Policy Requirements:\n{policy}\n\nObserved System:\n{system}")
    ])

    # Create the chain: prompt -> structured LLM
    chain = prompt | structured_llm

    # --- Step 4: Run and Verify ---
    print("\nAnalyzing system compliance...\n")
    result = chain.invoke({"policy": policy_text, "system": observed_system})
    
    # The result is a Pydantic object, not a string!
    print(f"Result Type: {type(result)}")
    print(f"Result is ComplianceReport: {isinstance(result, ComplianceReport)}")
    print("\n" + "="*60)
    print("COMPLIANCE REPORT")
    print("="*60)
    print(f"Policy: {result.policy_name}")
    print(f"Compliant: {'✅ YES' if result.compliant else '❌ NO'}")
    print(f"Confidence: {result.confidence_score:.1%}")
    print(f"\nMissing Controls:")
    for i, control in enumerate(result.missing_controls, 1):
        print(f"  {i}. {control}")
    
    # Demonstrate structured access
    print("\n" + "="*60)
    print("STRUCTURED DATA ACCESS")
    print("="*60)
    print(f"Can access as Python object:")
    print(f"  result.compliant = {result.compliant}")
    print(f"  result.confidence_score = {result.confidence_score}")
    print(f"  len(result.missing_controls) = {len(result.missing_controls)}")
    
    # Can also convert to dict or JSON
    print(f"\nAs dictionary:")
    print(f"  {result.model_dump()}")

if __name__ == "__main__":
    run_lab_2_1()
