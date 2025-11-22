# Lab 2.2: LlamaIndex for Complex Policy RAG

## Goal

Learn how to use **LlamaIndex** to ingest and query complex, unstructured documents (like PDF policies with tables and headers). This is crucial for the "Control Discovery" part of your Judge Agent.

## Concepts

### 1. LlamaIndex vs. LangChain

* **LangChain**: Great for orchestration and flows.
* **LlamaIndex**: Specialized for **Data Ingestion** and **Indexing**. It excels at parsing complex documents and creating hierarchical indices.

### 2. VectorStoreIndex

The standard index type. It chunks your text, embeds it, and stores it in a vector store (like Pinecone or local memory).

### 3. Query Engine

LlamaIndex provides a high-level `QueryEngine` API that handles retrieval and answer synthesis automatically.

```python
query_engine = index.as_query_engine()
response = query_engine.query("What is the policy on encryption?")
```

## Instructions

1. **Open `lab_2_2_starter.py`**.
2. **Step 1**: Load the sample data (`data/nist_rmf_gov.md`) using `SimpleDirectoryReader`.
3. **Step 2**: Create a `VectorStoreIndex` from the documents.
4. **Step 3**: Create a query engine and ask a question about "Governance".
5. **Step 4**: (Optional) Persist the index to disk so you don't have to rebuild it.

## Resources

* [LlamaIndex Documentation](https://docs.llamaindex.ai/en/stable/)
