import json
from pydantic import BaseModel, Field

class FinancialReport(BaseModel):
    project_name: str
    projected_revenue: float
    projected_cost: float
    roi: float = Field(description="(Revenue - Cost) / Cost")

def calculate_adjusted_roi(roi: float, risk_score: float) -> float:
    """
    TODO: Implement the formula: ROI * (1 - Risk Score)
    """
    pass

def roi_agent(financial_json: str, risk_score: float):
    print(f"--- ROI Agent Processing ---")
    print(f"Risk Score: {risk_score}")
    
    # 1. Parse JSON
    # data = json.loads(financial_json)
    # report = FinancialReport(**data)
    
    # 2. Calculate Adjusted ROI
    # adj_roi = ...
    
    # 3. Decision Logic (Threshold > 0.15)
    # if adj_roi > 0.15: ...
    pass

if __name__ == "__main__":
    sample_data = '{"project_name": "AI Upgrade", "projected_revenue": 150000, "projected_cost": 100000, "roi": 0.5}'
    risk_score = 0.4 # High risk
    
    roi_agent(sample_data, risk_score)
