import os
from typing import List
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
# You might need to install PyGithub: pip install PyGithub
from github import Github 

# Note: Ensure GITHUB_TOKEN and OPENAI_API_KEY are set
# os.environ["GITHUB_TOKEN"] = "ghp_..."

TARGET_REPO = "hwchase17/langchain" # Example public repo (or pick a smaller one)
# Better example for a small agent: "crewAIInc/crewAI-examples"

def fetch_repo_files(repo_name: str) -> List[Document]:
    """
    TODO: Fetch python files from a GitHub repo.
    1. Auth with Github(token).
    2. Get the repo object.
    3. Walk through files (recursively if needed) and get content.
    4. Return list of Document objects.
    """
    print(f"--- Fetching files from {repo_name} ---")
    token = os.environ.get("GITHUB_TOKEN")
    # g = Github(token)
    # repo = g.get_repo(repo_name)
    
    docs = []
    # YOUR CODE HERE
    # contents = repo.get_contents("")
    # ...
    
    return docs

def analyze_code(docs: List[Document]):
    """
    TODO: Analyze the code for security issues.
    1. Create a ChatOpenAI instance.
    2. Create a prompt that asks "Does this code contain hardcoded secrets?"
    3. Run it on the documents.
    """
    print("--- Analyzing Code ---")
    llm = ChatOpenAI(temperature=0)
    
    # YOUR CODE HERE
    pass

if __name__ == "__main__":
    # 1. Fetch
    # docs = fetch_repo_files("crewAIInc/crewAI-examples")
    
    # 2. Analyze
    # if docs:
    #     analyze_code(docs)
    pass
