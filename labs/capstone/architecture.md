# Capstone: Enterprise Risk Assessment System

## Overview

This is the final project where you combine all your agents into a cohesive system.

## Architecture

```mermaid
graph TD
    User[User Request] --> Orchestrator[LangGraph Orchestrator]
    
    Orchestrator --> ControlAgent[Control Discovery (RAG)]
    Orchestrator --> ThreatAgent[Threat Modeling (Markov)]
    Orchestrator --> ROIAgent[ROI Agent (Financial)]
    
    ControlAgent --> Context[Shared Context]
    ThreatAgent --> Context
    ROIAgent --> Context
    
    Context --> Judge[Judge Agent (Quality Gate)]
    
    Judge -- "Reject" --> Orchestrator
    Judge -- "Approve" --> Report[Final Report]
```

## Components

1. **Control Discovery Agent**: Uses **LlamaIndex** (Lab 2.2) to find relevant security controls in the `nist_rmf_gov.md` file.
2. **Threat Modeling Agent**: Uses **Markov Chains** (Lab 5.2) to generate a likely attack path for the system.
3. **ROI Agent**: Uses **Pandas/Pydantic** (Lab 2.3) to calculate if the project is financially viable given the risk.
4. **Judge Agent**: Uses **DSPy** (Lab 4.1) or **Pydantic** (Lab 2.1) to evaluate the findings from the other three agents.
5. **Orchestrator**: A **LangGraph** (Lab 1.2) workflow that manages the parallel execution and the feedback loop.

## Implementation Steps

1. Define the `AgentState` (TypedDict) to hold:
    * `controls`: List[str]
    * `attack_path`: List[str]
    * `roi_decision`: str
    * `judge_feedback`: str
2. Create Nodes for each agent.
3. Create the Graph with a conditional edge from `Judge` -> `End` or `Judge` -> `Retry`.
