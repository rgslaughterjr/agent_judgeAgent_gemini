import os
import time
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from pinecone import Pinecone, ServerlessSpec

# Note: Ensure OPENAI_API_KEY and PINECONE_API_KEY are set
# os.environ["OPENAI_API_KEY"] = "sk-..."
# os.environ["PINECONE_API_KEY"] = "pc-..."

def run_lab_1_3():
    print("### Lab 1.3: Compliance RAG (PineCone + LangChain) ###")
    
    # 1. Setup Pinecone
    pc_api_key = os.environ.get("PINECONE_API_KEY")
    if not pc_api_key:
        print("ERROR: PINECONE_API_KEY not found. Skipping Lab 1.3 execution.")
        return

    pc = Pinecone(api_key=pc_api_key)
    index_name = "nist-compliance-lab"
    
    # Check if index exists, create if not
    existing_indexes = [i.name for i in pc.list_indexes()]
    if index_name not in existing_indexes:
        print(f"Creating Pinecone index: {index_name}...")
        pc.create_index(
            name=index_name,
            dimension=1536, # OpenAI embedding dimension
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        time.sleep(2) # Wait for initialization

    # 2. Ingest Data (Simulated NIST RMF Content)
    print("Ingesting NIST AI RMF content...")
    nist_text = """
    NIST AI RMF Core Functions:
    1. GOVERN: A culture of risk management is cultivated and present. Governance processes are in place.
    2. MAP: Context is established and risks related to the AI system are identified and enhanced.
    3. MEASURE: Identified risks are assessed, analyzed, and tracked.
    4. MANAGE: Risks are prioritized and acted upon based on a projected impact.
    
    Specific Control GOVERN 1.1: Legal and regulatory requirements involving AI are understood and managed.
    Specific Control MAP 1.2: Intended purposes, potentially beneficial uses, and context-specific laws, norms and expectations are understood and documented.
    """
    
    docs = [Document(page_content=nist_text, metadata={"source": "NIST_AI_RMF_1.0_Snippet"})]
    
    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index_name=index_name
    )
    
    # 3. Create RAG Chain
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    
    template = """Answer the question based only on the following context:
    {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # 4. Ask Questions
    query = "What is the purpose of the MAP function?"
    print(f"\nQuery: {query}")
    response = chain.invoke(query)
    print(f"Response: {response}")
    
    query2 = "Explain GOVERN 1.1"
    print(f"\nQuery: {query2}")
    response2 = chain.invoke(query2)
    print(f"Response: {response2}")

if __name__ == "__main__":
    run_lab_1_3()
