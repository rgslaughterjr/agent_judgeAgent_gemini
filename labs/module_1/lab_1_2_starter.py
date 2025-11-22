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
    TODO: Check the last message for PII keywords (e.g., 'SSN').
    Return {'pii_detected': True/False}
    """
    print("--- Node: Checking for PII ---")
    # messages = state['messages']
    # last_msg = messages[-1].content
    
    # YOUR CODE HERE
    
    return {"pii_detected": False} # Placeholder

def redact_node(state: AgentState):
    """
    TODO: Return a blocked message.
    """
    print("--- Node: Redacting ---")
    return {"messages": [AIMessage(content="BLOCKED: PII Detected.")]}

def process_node(state: AgentState):
    """
    TODO: Process the safe message (Mock LLM response).
    """
    print("--- Node: Processing ---")
    return {"messages": [AIMessage(content="Processed safely.")]}

# --- Router ---

def route_pii(state: AgentState):
    """
    TODO: Return 'redact' if pii_detected is True, else 'process'.
    """
    # if state['pii_detected']: ...
    return "process" # Placeholder

# --- Graph Construction ---

def build_graph():
    # workflow = StateGraph(AgentState)
    
    # TODO: Add Nodes
    # workflow.add_node("check_pii", check_pii_node)
    # ...

    # TODO: Set Entry Point
    # workflow.set_entry_point("check_pii")

    # TODO: Add Conditional Edges
    # workflow.add_conditional_edges(
    #     "check_pii",
    #     route_pii,
    #     {"redact": "redact", "process": "process"}
    # )

    # TODO: Add Edges to END
    # workflow.add_edge("redact", END)
    # ...

    # return workflow.compile()
    pass

def run_lab_1_2():
    print("### Lab 1.2: PII Router (LangGraph) ###")
    # app = build_graph()

    # Test 1: Safe
    print("\n--- Test 1: Safe ---")
    # inputs = {"messages": [HumanMessage(content="Hello world")]}
    # for output in app.stream(inputs): pass

    # Test 2: PII
    print("\n--- Test 2: PII ---")
    # inputs = {"messages": [HumanMessage(content="My SSN is 123")]}
    # for output in app.stream(inputs): pass

if __name__ == "__main__":
    run_lab_1_2()
