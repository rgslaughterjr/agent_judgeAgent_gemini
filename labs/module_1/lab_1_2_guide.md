# Lab 1.2: PII Router (LangGraph)

## Goal

Learn how to build a stateful workflow using **LangGraph** that routes user input based on security checks (PII Detection).

## Concepts

### 1. State (`TypedDict`)

The **State** is the memory of your graph. It is passed between nodes.

```python
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    pii_detected: bool
```

### 2. Nodes

**Nodes** are python functions that perform work. They take the current state as input and return an update to the state.

* `check_pii_node`: Scans the latest message for sensitive info.
* `redact_node`: Returns a "BLOCKED" message if PII is found.
* `process_node`: Processes the message if it's safe.

### 3. Conditional Edges (The Router)

Instead of a fixed path (A -> B), **Conditional Edges** let you choose the next node dynamically.

* `route_pii`: Looks at `state['pii_detected']`. If True -> go to `redact`. If False -> go to `process`.

## Instructions

1. **Open `lab_1_2_starter.py`**.
2. **Step 1**: Implement `check_pii_node`. Check `state['messages'][-1]` for keywords like "SSN" or "Credit Card". Update `pii_detected` in the return value.
3. **Step 2**: Implement `redact_node` and `process_node`.
4. **Step 3**: Implement the `route_pii` function logic.
5. **Step 4**: Build the graph using `StateGraph`. Add nodes, set the entry point, and add the conditional edge.
6. **Step 5**: Compile and run the graph with test inputs.

## Resources

* [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
