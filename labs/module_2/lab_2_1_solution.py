from typing import List
from pydantic import BaseModel, Field, field_validator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# --- Step 1: Define the Schema ---
class ComplianceReport(BaseModel):
    policy_name: str = Field(description="The name of the policy being analyzed")
    compliant: bool = Field(description="True if the system meets all requirements, else False")
    confidence_score: float = Field(description="Confidence in the assessment, from 0.0 to 1.0")
    missing_controls: List[str] = Field(description="List of specific controls that are missing or failed")
    reasoning: str = Field(description="Brief explanation of the findings")

    # --- Step 2: Add Validators ---
    @field_validator('confidence_score')
    @classmethod
    def check_score(cls, v):
        if v < 0.0 or v > 1.0:
            raise ValueError("Confidence score must be between 0.0 and 1.0")
        return v

def run_lab_2_1():
    print("### Lab 2.1: Pydantic Validators (Solution) ###")
    
    policy_text = """
    The system must encrypt all data at rest using AES-256.
    Multi-factor authentication is required for all admin access.
    """
    
    observed_system = """
    The database is encrypted with AES-256.
    Admin access uses a simple password.
    """

    # --- Step 3: Create Chain ---
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Bind the schema to the LLM
    structured_llm = llm.with_structured_output(ComplianceReport)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a strict compliance auditor. Analyze the system against the policy."),
        ("user", "Policy: {policy}\nSystem: {system}")
    ])

    chain = prompt | structured_llm

    # --- Step 4: Run ---
    print("Analyzing system...")
    result = chain.invoke({"policy": policy_text, "system": observed_system})
    
    print(f"\n--- Report Generated ---")
    print(f"Policy: {result.policy_name}")
    print(f"Compliant: {result.compliant}")
    print(f"Score: {result.confidence_score}")
    print(f"Missing Controls: {result.missing_controls}")
    print(f"Reasoning: {result.reasoning}")

if __name__ == "__main__":
    run_lab_2_1()
