from typing import List
from pydantic import BaseModel, Field, field_validator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Note: Ensure OPENAI_API_KEY is set

# --- Step 1: Define the Schema ---
class ComplianceReport(BaseModel):
    """
    TODO: Define the schema for a compliance report.
    Fields needed:
    - policy_name: str
    - compliant: bool
    - confidence_score: float (0.0 to 1.0)
    - missing_controls: List[str]
    """
    # policy_name: str = Field(description="The name of the policy being analyzed")
    # ...
    pass

    # --- Step 2: Add Validators ---
    # @field_validator('confidence_score')
    # @classmethod
    # def check_score(cls, v):
    #     if v < 0 or v > 1:
    #         raise ValueError("Score must be between 0 and 1")
    #     return v

def run_lab_2_1():
    print("### Lab 2.1: Pydantic Validators ###")
    
    # Sample Input
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
    
    # TODO: Bind the schema to the LLM
    # structured_llm = llm.with_structured_output(ComplianceReport)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a strict compliance auditor. Analyze the system against the policy."),
        ("user", "Policy: {policy}\nSystem: {system}")
    ])

    # chain = prompt | structured_llm

    # --- Step 4: Run ---
    print("Analyzing system...")
    # result = chain.invoke({"policy": policy_text, "system": observed_system})
    
    # print(f"Result Type: {type(result)}")
    # print(result)
    
    # Verify it's a Pydantic object
    # if isinstance(result, ComplianceReport):
    #     print(f"Is Compliant? {result.compliant}")
    #     print(f"Missing: {result.missing_controls}")

if __name__ == "__main__":
    run_lab_2_1()
