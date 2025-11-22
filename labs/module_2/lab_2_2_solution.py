import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI

# Set global settings
Settings.llm = OpenAI(model="gpt-4o", temperature=0)

def run_lab_2_2():
    print("### Lab 2.2: LlamaIndex RAG (Solution) ###")
    
    data_path = "../../data/nist_rmf_gov.md"
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        return

    # --- Step 1: Load Data ---
    print(f"Loading data from {data_path}...")
    documents = SimpleDirectoryReader(input_files=[data_path]).load_data()
    print(f"Loaded {len(documents)} documents.")
    
    # --- Step 2: Create Index ---
    print("Creating VectorStoreIndex...")
    index = VectorStoreIndex.from_documents(documents)
    
    # --- Step 3: Query ---
    print("Querying: 'What are the primary outcomes of the GOVERN function?'")
    query_engine = index.as_query_engine()
    response = query_engine.query("What are the primary outcomes of the GOVERN function?")
    
    print(f"\nResponse:\n{response}")

if __name__ == "__main__":
    run_lab_2_2()
