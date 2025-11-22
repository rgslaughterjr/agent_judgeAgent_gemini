from typing import TypedDict, List, Annotated
import operator
from langgraph.graph import StateGraph, END

# Define State
class AgentState(TypedDict):
    controls: List[str]
    attack_path: List[str]
    roi_decision: str
    judge_feedback: str
    approved: bool

# --- Nodes ---

def control_discovery_node(state: AgentState):
    print("--- Control Discovery ---")
    # TODO: Call LlamaIndex Agent
    return {"controls": ["Control A", "Control B"]}

def threat_modeling_node(state: AgentState):
    print("--- Threat Modeling ---")
    # TODO: Call Markov Chain
    return {"attack_path": ["Recon", "Access", "Done"]}

def roi_node(state: AgentState):
    print("--- ROI Analysis ---")
    # TODO: Call ROI Agent
    return {"roi_decision": "Approve"}

def judge_node(state: AgentState):
    print("--- Judge Evaluation ---")
    # TODO: Evaluate consistency
    # If controls are weak but ROI is high -> What do we do?
    return {"approved": True, "judge_feedback": "Looks good."}

# --- Graph ---

def run_capstone():
    print("### Capstone: Enterprise Risk Assessment System ###")
    
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("control_discovery", control_discovery_node)
    workflow.add_node("threat_modeling", threat_modeling_node)
    workflow.add_node("roi_analysis", roi_node)
    workflow.add_node("judge", judge_node)
    
    # Edges (Parallel Execution)
    workflow.set_entry_point("control_discovery")
    workflow.add_edge("control_discovery", "threat_modeling") # Sequential for simplicity, can be parallel
    workflow.add_edge("threat_modeling", "roi_analysis")
    workflow.add_edge("roi_analysis", "judge")
    workflow.add_edge("judge", END)
    
    app = workflow.compile()
    
    # Run
    result = app.invoke({})
    print(f"Final Result: {result}")

if __name__ == "__main__":
    run_capstone()
