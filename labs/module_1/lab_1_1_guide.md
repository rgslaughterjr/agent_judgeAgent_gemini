# Lab 1.1: Security Researcher (LangGraph)

## Goal

Learn the fundamentals of **LangGraph** by building a simple sequential workflow: A Researcher agent passes information to a Writer agent.

## Concepts

### 1. State (`TypedDict`)

The **State** is the shared memory of your graph. It holds the data that agents read and write to.

```python
class AgentState(TypedDict):
    topic: str
    research_findings: str
    summary: str
```

### 2. Nodes

**Nodes** are Python functions that perform work. They take the current `State` as input and return a dictionary to *update* the state.

* `research_node`: Takes `topic`, produces `research_findings`.
* `writer_node`: Takes `research_findings`, produces `summary`.

### 3. Edges

**Edges** define the flow of control.

* **Sequential Edge**: `researcher` -> `writer`. This means "After the researcher finishes, go immediately to the writer."

## Instructions

1. **Open `lab_1_1_starter.py`**.
2. **Review the State**: Look at how `AgentState` is defined.
3. **Review the Nodes**: See how `research_node` and `writer_node` use the LLM to process data.
4. **Review the Graph**: Notice how `workflow.add_edge("researcher", "writer")` connects the two agents.
5. **Run the Lab**: Execute the script to see the agents work in sequence.

## Resources

* [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
