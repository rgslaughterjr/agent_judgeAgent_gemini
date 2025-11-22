import os
# pip install llama-index
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI

# Ensure OPENAI_API_KEY is set
# Settings.llm = OpenAI(model="gpt-4o")

def run_lab_2_2():
    print("### Lab 2.2: LlamaIndex RAG ###")
    
    # --- Step 1: Load Data ---
    print("Loading data...")
    # documents = SimpleDirectoryReader(input_files=["../../data/nist_rmf_gov.md"]).load_data()
    
    # --- Step 2: Create Index ---
    print("Creating index...")
    # index = VectorStoreIndex.from_documents(documents)
    
    # --- Step 3: Query ---
    # query_engine = index.as_query_engine()
    # response = query_engine.query("Summarize the GOVERN function.")
    
    # print(f"\nResponse:\n{response}")

if __name__ == "__main__":
    run_lab_2_2()
