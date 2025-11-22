import json
from pydantic import BaseModel, Field

class FinancialReport(BaseModel):
    project_name: str
    projected_revenue: float
    projected_cost: float
    roi: float = Field(description="(Revenue - Cost) / Cost")

def calculate_adjusted_roi(roi: float, risk_score: float) -> float:
    """
    Formula: ROI * (1 - Risk Score)
    """
    return roi * (1.0 - risk_score)

def roi_agent(financial_json: str, risk_score: float):
    print(f"--- ROI Agent Processing ---")
    print(f"Input Data: {financial_json}")
    print(f"Risk Score: {risk_score}")
    
    try:
        # 1. Parse JSON
        data = json.loads(financial_json)
        report = FinancialReport(**data)
        print(f"Parsed Report: {report.project_name} (Base ROI: {report.roi:.2%})")
        
        # 2. Calculate Adjusted ROI
        adj_roi = calculate_adjusted_roi(report.roi, risk_score)
        print(f"Risk-Adjusted ROI: {adj_roi:.2%}")
        
        # 3. Decision Logic (Threshold > 0.15)
        threshold = 0.15
        if adj_roi > threshold:
            print("✅ DECISION: APPROVE (ROI exceeds hurdle rate)")
        else:
            print("❌ DECISION: REJECT (ROI too low for risk level)")
            
    except Exception as e:
        print(f"Error processing financial data: {e}")

if __name__ == "__main__":
    # Scenario 1: High ROI, High Risk
    sample_data = '{"project_name": "AI Upgrade", "projected_revenue": 150000, "projected_cost": 100000, "roi": 0.5}'
    risk_score = 0.4 
    roi_agent(sample_data, risk_score)
    
    print("-" * 20)
    
    # Scenario 2: Low ROI, Low Risk
    sample_data_2 = '{"project_name": "Legacy Maintenance", "projected_revenue": 110000, "projected_cost": 100000, "roi": 0.1}'
    risk_score_2 = 0.1
    roi_agent(sample_data_2, risk_score_2)
