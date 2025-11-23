import operator
from typing import Annotated, TypedDict, Union
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, END

# --- State Definition ---
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    pii_detected: bool

# --- Nodes ---

def check_pii_node(state: AgentState):
    """
    Check the last message for PII keywords (e.g., 'SSN').
    Return {'pii_detected': True/False}
    """
    print("--- Node: Checking for PII ---")
    messages = state['messages']
    last_msg = messages[-1].content
    
    if "SSN" in last_msg or "Credit Card" in last_msg:
        print("  [!] PII Detected!")
        return {"pii_detected": True}
    
    print("  [+] No PII found.")
    return {"pii_detected": False}

def redact_node(state: AgentState):
    """
    Return a blocked message.
    """
    print("--- Node: Redacting ---")
    return {"messages": [AIMessage(content="BLOCKED: PII Detected.")]}

def process_node(state: AgentState):
    """
    Process the safe message (Mock LLM response).
    """
    print("--- Node: Processing ---")
    return {"messages": [AIMessage(content="Processed safely.")]}

# --- Router ---

def route_pii(state: AgentState):
    """
    Return 'redact' if pii_detected is True, else 'process'.
    """
    if state['pii_detected']:
        return "redact"
    return "process"

# --- Graph Construction ---

def build_graph():
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("check_pii", check_pii_node)
    workflow.add_node("redact", redact_node)
    workflow.add_node("process", process_node)

    # Set Entry Point
    workflow.set_entry_point("check_pii")

    # Add Conditional Edges
    workflow.add_conditional_edges(
        "check_pii",
        route_pii,
        {"redact": "redact", "process": "process"}
    )

    # Add Edges to END
    workflow.add_edge("redact", END)
    workflow.add_edge("process", END)

    return workflow.compile()

def run_lab_1_2():
    print("### Lab 1.2: PII Router (LangGraph) ###")
    app = build_graph()

    # Test 1: Safe
    print("\n--- Test 1: Safe ---")
    inputs = {"messages": [HumanMessage(content="Hello world")]}
    for output in app.stream(inputs): pass

    # Test 2: PII
    print("\n--- Test 2: PII ---")
    inputs = {"messages": [HumanMessage(content="My SSN is 123")]}
    for output in app.stream(inputs): pass

if __name__ == "__main__":
    run_lab_1_2()
