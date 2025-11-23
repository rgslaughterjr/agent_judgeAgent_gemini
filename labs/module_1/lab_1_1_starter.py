import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

# --- Step 1: Define State ---
class AgentState(TypedDict):
    topic: str
    research_findings: str
    summary: str

# --- Step 2: Define Nodes ---
def research_node(state: AgentState):
    """
    Agent 1: The Researcher
    Role: Analyze the topic and produce detailed findings.
    """
    print(f"\n--- [Researcher] Analyzing: {state['topic']} ---")
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    messages = [
        SystemMessage(content="You are a senior security analyst specializing in AI governance. Provide detailed, bulleted findings on the requested topic."),
        HumanMessage(content=f"Research the following topic: {state['topic']}")
    ]
    
    response = llm.invoke(messages)
    return {"research_findings": response.content}

def writer_node(state: AgentState):
    """
    Agent 2: The Writer
    Role: Summarize the findings for a non-technical audience.
    """
    print("\n--- [Writer] Drafting Summary ---")
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    messages = [
        SystemMessage(content="You are a technical writer. Summarize the provided technical findings into a concise executive summary."),
        HumanMessage(content=f"Here are the findings:\n\n{state['research_findings']}")
    ]
    
    response = llm.invoke(messages)
    return {"summary": response.content}

# --- Step 3: Build & Run Graph ---
def run_lab_1_1():
    print("### Lab 1.1: Security Researcher (LangGraph) ###")
    
    # 1. Initialize Graph
    workflow = StateGraph(AgentState)
    
    # 2. Add Nodes
    workflow.add_node("researcher", research_node)
    workflow.add_node("writer", writer_node)
    
    # 3. Define Edges (The Workflow)
    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", END)
    
    # 4. Compile
    app = workflow.compile()
    
    # 5. Execute
    initial_state = {"topic": "NIST AI RMF 'GOVERN' function"}
    print(f"Starting workflow with input: {initial_state['topic']}")
    
    result = app.invoke(initial_state)
    
    print("\n" + "="*50)
    print("RESEARCH FINDINGS")
    print("="*50)
    print(result['research_findings'])
    
    print("\n" + "="*50)
    print("FINAL EXECUTIVE SUMMARY")
    print("="*50)
    print(result['summary'])

if __name__ == "__main__":
    run_lab_1_1()
