import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pinecone import Pinecone, ServerlessSpec
import time

# Load environment variables
load_dotenv()

def run_lab_1_3():
    print("--- Lab 1.3: Advanced RAG & Retrieval Strategies ---")

    # --- Step 1: Load Documents ---
    print("\n[1] Loading Documents...")
    try:
        # Load the internal policy and NIST RMF guide
        # Assuming running from project root
        loader_policy = TextLoader("data/internal_ai_policy.txt")
        loader_nist = TextLoader("data/nist_rmf_gov.md")
        
        docs_policy = loader_policy.load()
        docs_nist = loader_nist.load()
        
        all_docs = docs_policy + docs_nist
        print(f"    Loaded {len(all_docs)} documents.")
    except Exception as e:
        print(f"    Error loading documents: {e}")
        print("    Make sure you are running this script from the project root!")
        return

    # --- Step 2: Split Documents (Chunking) ---
    print("\n[2] Splitting Documents...")
    # We use a recursive splitter to keep related text together
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(all_docs)
    print(f"    Created {len(splits)} chunks.")

    # --- Step 3: Initialize Embeddings & Vector Store (Pinecone) ---
    print("\n[3] Setting up Vector Store (Pinecone)...")
    
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    if not pinecone_api_key:
        print("    ERROR: PINECONE_API_KEY not found in .env")
        return

    index_name = "agent-judge-labs"
    
    # Initialize Pinecone client to check/create index
    pc = Pinecone(api_key=pinecone_api_key)
    
    # Check if index exists, if not create it
    existing_indexes = [index.name for index in pc.list_indexes()]
    if index_name not in existing_indexes:
        print(f"    Index '{index_name}' not found. Creating...")
        pc.create_index(
            name=index_name,
            dimension=1536, # OpenAI text-embedding-3-small dimension
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        # Wait for index to be ready
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)
        print("    Index created.")
    else:
        print(f"    Index '{index_name}' already exists.")

    # Initialize Embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # Create Vector Store and upload documents
    print("    Upserting documents to Pinecone (this may take a moment)...")
    vectorstore = PineconeVectorStore.from_documents(
        documents=splits,
        embedding=embeddings,
        index_name=index_name
    )
    print("    Documents stored successfully.")

    # --- Step 4: Multi-Query Retrieval ---
    print("\n[4] Setting up Multi-Query Retriever...")
    
    # The LLM used to generate alternative queries
    llm = ChatOpenAI(temperature=0)
    
    retriever = MultiQueryRetriever.from_llm(
        retriever=vectorstore.as_retriever(),
        llm=llm
    )

    # --- Step 5: RAG Chain ---
    print("\n[5] Running RAG Chain...")
    
    # Define the prompt template
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # Build the chain
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # Test Question
    question = "What are the requirements for AI model approval according to the internal policy?"
    print(f"\n    Question: {question}")
    print("    Thinking...")
    
    response = chain.invoke(question)
    
    print("\n    Answer:")
    print(f"    {response}")

if __name__ == "__main__":
    run_lab_1_3()
