import os
import time
from typing import List
from langchain_community.document_loaders import DirectoryLoader, TextLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document
from pinecone import Pinecone, ServerlessSpec

# --- Configuration ---
INDEX_NAME = "agent-judge-lab-1-3"
DATA_DIR = "../../data"

def load_documents() -> List[Document]:
    print("--- Loading Documents ---")
    # We use DirectoryLoader which defaults to UnstructuredLoader, but for specific control:
    # We can load specific extensions.
    loaders = [
        DirectoryLoader(DATA_DIR, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader),
        DirectoryLoader(DATA_DIR, glob="**/*.txt", loader_cls=TextLoader),
        # JSON loading can be tricky with schemas, treating as text for simplicity in this lab
        DirectoryLoader(DATA_DIR, glob="**/*.json", loader_cls=TextLoader) 
    ]
    
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    
    print(f"Loaded {len(docs)} documents.")
    return docs

def split_documents(docs: List[Document]) -> List[Document]:
    print("--- Splitting Documents ---")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    splits = text_splitter.split_documents(docs)
    print(f"Created {len(splits)} chunks.")
    return splits

def setup_vectorstore(splits: List[Document]):
    print("--- Setting up VectorStore ---")
    pc = Pinecone()
    
    existing_indexes = [i.name for i in pc.list_indexes()]
    if INDEX_NAME not in existing_indexes:
        print(f"Creating index {INDEX_NAME}...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        time.sleep(10)

    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore.from_documents(
        documents=splits,
        embedding=embeddings,
        index_name=INDEX_NAME
    )
    return vectorstore

def run_queries(vectorstore):
    llm = ChatOpenAI(temperature=0)
    
    # 1. Basic Retrieval
    print("\n--- Basic Retrieval ---")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    query = "What are the prohibited AI models?"
    docs = retriever.invoke(query)
    for i, doc in enumerate(docs):
        print(f"Result {i+1}: {doc.page_content[:100]}... (Source: {doc.metadata.get('source')})")

    # 2. Multi-Query Retrieval
    print("\n--- Multi-Query Retrieval ---")
    mq_retriever = MultiQueryRetriever.from_llm(
        retriever=vectorstore.as_retriever(),
        llm=llm
    )
    complex_query = "Compare the NIST GOVERN requirements with our internal policy on PII."
    
    # Enable logging to see the generated queries
    import logging
    logging.basicConfig()
    logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)
    
    docs = mq_retriever.invoke(complex_query)
    print(f"\nRetrieved {len(docs)} documents for complex query.")
    for i, doc in enumerate(docs):
        print(f"Result {i+1}: {doc.page_content[:100]}... (Source: {doc.metadata.get('source')})")

if __name__ == "__main__":
    docs = load_documents()
    if docs:
        splits = split_documents(docs)
        vectorstore = setup_vectorstore(splits)
        run_queries(vectorstore)
