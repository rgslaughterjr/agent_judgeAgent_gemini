# Lab 1.3: Advanced RAG & Retrieval Strategies

## Goal

Learn how to build a robust Retrieval Augmented Generation (RAG) system that can handle:

1. **Mixed Data Formats**: Ingesting Markdown, Text, and JSON.
2. **Metadata Filtering**: Narrowing down search results based on file type or date (critical for compliance).
3. **Multi-Query Retrieval**: Handling complex questions by breaking them down into sub-queries.

## Concepts

### 1. Dense vs. Sparse Embeddings

* **Dense Embeddings** (e.g., OpenAI `text-embedding-3-small`): Capture *semantic meaning*. Good for "concept matching".
* **Sparse Embeddings** (e.g., BM25, SPLADE): Capture *keyword frequency*. Good for "exact phrase matching" (like specific error codes or regulation IDs).
* *In this lab, we will focus on Dense Embeddings with PineCone.*

### 2. Metadata Filtering

When you index documents, you don't just store the text. You store metadata:

```json
{
  "text": "Do not input PII...",
  "source": "internal_ai_policy.txt",
  "year": 2024,
  "category": "policy"
}
```

This allows you to ask: *"What is the policy on PII?"* AND filter by `year == 2024`. This reduces hallucinations by restricting the search space.

### 3. Multi-Query Retrieval

Users often ask complex questions: *"Compare the NIST requirements for Governance with our internal policy on PII."*
A simple vector search might fail because it tries to find one document matching both.
**Multi-Query** breaks this into:

1. *"What are NIST requirements for Governance?"*
2. *"What is the internal policy on PII?"*
It retrieves documents for *both* and combines the context.

## Instructions

1. **Open `lab_1_3_starter.py`**.
2. **Step 1**: Implement the `load_documents()` function. Use `DirectoryLoader` to load files from the `data/` folder.
3. **Step 2**: Implement `ingest_documents()`. Split the text into chunks and upload to PineCone. **Crucial**: Add metadata to each chunk (e.g., filename).
4. **Step 3**: Implement `get_retriever()`. Create a standard vector store retriever.
5. **Step 4**: Implement `get_multi_query_retriever()`. Use LangChain's `MultiQueryRetriever` to enhance the basic retriever.
6. **Step 5**: Run the lab and compare the results of a simple query vs. a complex query.

## Resources

* [LangChain DirectoryLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/file_directory)
* [PineCone Filtering](https://docs.pinecone.io/docs/metadata-filtering)
* [LangChain MultiQueryRetriever](https://python.langchain.com/docs/modules/data_connection/retrievers/MultiQueryRetriever)
