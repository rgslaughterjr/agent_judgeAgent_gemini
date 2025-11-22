import os
import time
from typing import List
from langchain_community.document_loaders import DirectoryLoader, TextLoader, UnstructuredMarkdownLoader, JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document
from pinecone import Pinecone, ServerlessSpec

# --- Configuration ---
INDEX_NAME = "agent-judge-lab-1-3"
DATA_DIR = "../../data" # Path to your data folder

def load_documents() -> List[Document]:
    """
    TODO: Load documents from the DATA_DIR.
    1. Use DirectoryLoader to load all files.
    2. Hint: You might need 'glob' parameters to find specific extensions if DirectoryLoader defaults fail.
    3. Alternatively, load each file type separately and combine the lists.
    """
    print("--- Loading Documents ---")
    docs = []
    # YOUR CODE HERE
    # docs = ...
    
    print(f"Loaded {len(docs)} documents.")
    return docs

def split_documents(docs: List[Document]) -> List[Document]:
    """
    TODO: Split documents into smaller chunks for embedding.
    1. Use RecursiveCharacterTextSplitter.
    2. Recommended chunk_size=1000, chunk_overlap=200.
    """
    print("--- Splitting Documents ---")
    splits = []
    # YOUR CODE HERE
    # splitter = ...
    # splits = ...
    
    print(f"Created {len(splits)} chunks.")
    return splits

def setup_vectorstore(splits: List[Document]):
    """
    Sets up the Pinecone VectorStore.
    (Boilerplate provided for you, but review how it works)
    """
    print("--- Setting up VectorStore ---")
    pc = Pinecone() # Uses PINECONE_API_KEY env var
    
    # Create index if not exists
    existing_indexes = [i.name for i in pc.list_indexes()]
    if INDEX_NAME not in existing_indexes:
        print(f"Creating index {INDEX_NAME}...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        time.sleep(10) # Wait for initialization

    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore.from_documents(
        documents=splits,
        embedding=embeddings,
        index_name=INDEX_NAME
    )
    return vectorstore

def run_queries(vectorstore):
    """
    TODO: Run retrieval queries.
    1. Create a basic retriever from the vectorstore.
    2. Create a MultiQueryRetriever.
    3. Ask a complex question and compare results.
    """
    llm = ChatOpenAI(temperature=0)
    
    # 1. Basic Retrieval
    print("\n--- Basic Retrieval ---")
    # retriever = ...
    # query = "What are the prohibited AI models?"
    # result = retriever.invoke(query)
    # print(result)

    # 2. Multi-Query Retrieval
    print("\n--- Multi-Query Retrieval ---")
    # mq_retriever = MultiQueryRetriever.from_llm(...)
    # complex_query = "Compare the NIST GOVERN requirements with our internal policy on PII."
    # result = mq_retriever.invoke(complex_query)
    # print(result)

if __name__ == "__main__":
    # 1. Load
    docs = load_documents()
    
    # 2. Split
    if docs:
        splits = split_documents(docs)
        
        # 3. Index
        # vectorstore = setup_vectorstore(splits)
        
        # 4. Query
        # run_queries(vectorstore)
    else:
        print("No documents loaded. Please implement load_documents() first.")
