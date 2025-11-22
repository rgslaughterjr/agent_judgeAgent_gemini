import operator
from typing import Annotated, TypedDict, Union
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, END

# Define the State
class AgentState(TypedDict):
    # The 'messages' key will hold a list of messages, and add_messages will append to it
    messages: Annotated[list[BaseMessage], operator.add]
    pii_detected: bool

# --- Nodes ---

def check_pii_node(state: AgentState):
    """
    Simulated PII detection node.
    Checks for keywords like 'SSN', 'Credit Card', 'Social Security'.
    """
    print("--- Node: Checking for PII ---")
    messages = state['messages']
    last_message = messages[-1].content
    
    # Simple keyword detection for simulation
    pii_keywords = ["SSN", "Social Security", "Credit Card", "1234-5678"]
    found_pii = any(keyword in last_message for keyword in pii_keywords)
    
    if found_pii:
        print(f"  [ALERT] PII Detected in message: '{last_message[:20]}...'")
    else:
        print("  [OK] No PII detected.")
        
    return {"pii_detected": found_pii}

def redact_node(state: AgentState):
    """
    Node to handle PII violations.
    """
    print("--- Node: Redacting/Blocking ---")
    return {"messages": [AIMessage(content="BLOCKED: Your message contains Sensitive PII and cannot be processed by the public model.")]}

def process_node(state: AgentState):
    """
    Node to process safe messages (Mock LLM call).
    """
    print("--- Node: Processing Safe Request ---")
    user_msg = state['messages'][-1].content
    # In a real app, you'd call an LLM here
    response = f"Processed: I received your request '{user_msg}' and it is safe to handle."
    return {"messages": [AIMessage(content=response)]}

# --- Conditional Logic ---

def route_pii(state: AgentState):
    """
    Router function to determine the next node.
    """
    if state['pii_detected']:
        return "redact"
    else:
        return "process"

# --- Graph Construction ---

def build_graph():
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("check_pii", check_pii_node)
    workflow.add_node("redact", redact_node)
    workflow.add_node("process", process_node)

    # Set entry point
    workflow.set_entry_point("check_pii")

    # Add conditional edges
    workflow.add_conditional_edges(
        "check_pii",
        route_pii,
        {
            "redact": "redact",
            "process": "process"
        }
    )

    # Add edges from leaf nodes to END
    workflow.add_edge("redact", END)
    workflow.add_edge("process", END)

    return workflow.compile()

def run_lab_1_2():
    print("### Lab 1.2: PII Router (LangGraph) ###")
    app = build_graph()

    # Test Case 1: Safe Input
    print("\n\n--- Test 1: Safe Input ---")
    inputs_safe = {"messages": [HumanMessage(content="Tell me about the NIST AI RMF.")]}
    for output in app.stream(inputs_safe):
        pass # The nodes print their status
    print(f"Final Output: {output}")

    # Test Case 2: PII Input
    print("\n\n--- Test 2: PII Input ---")
    inputs_pii = {"messages": [HumanMessage(content="My Social Security Number is 123-45-6789.")]}
    for output in app.stream(inputs_pii):
        pass
    print(f"Final Output: {output}")

if __name__ == "__main__":
    run_lab_1_2()
