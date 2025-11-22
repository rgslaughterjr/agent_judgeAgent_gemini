import os
from typing import List
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from github import Github, Auth

# Target a specific folder in a repo to avoid fetching too much for the demo
TARGET_REPO = "crewAIInc/crewAI-examples"
TARGET_PATH = "instagram_search" # Specific example folder

def fetch_repo_files(repo_name: str, path: str) -> List[Document]:
    print(f"--- Fetching files from {repo_name}/{path} ---")
    
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        auth = Auth.Token(token)
        g = Github(auth=auth)
    else:
        print("Warning: No GITHUB_TOKEN found. Rate limits may apply.")
        g = Github()

    try:
        repo = g.get_repo(repo_name)
        contents = repo.get_contents(path)
    except Exception as e:
        print(f"Error fetching repo: {e}")
        return []

    docs = []
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            if file_content.name.endswith(".py"):
                print(f"Found file: {file_content.path}")
                # Decode content
                try:
                    text = file_content.decoded_content.decode("utf-8")
                    docs.append(Document(page_content=text, metadata={"source": file_content.path}))
                except:
                    print(f"Could not decode {file_content.path}")
    
    print(f"Fetched {len(docs)} Python files.")
    return docs

def analyze_code(docs: List[Document]):
    print("--- Analyzing Code ---")
    llm = ChatOpenAI(temperature=0)
    
    template = """You are a Security Auditor. Analyze the following python code for security risks.
    Specifically look for:
    1. Hardcoded API keys or secrets.
    2. Use of dangerous functions like eval() or exec().
    3. Insecure network calls (http vs https).

    Code File: {source}
    Content:
    {content}

    Report:
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    for doc in docs[:3]: # Analyze first 3 files to save tokens
        print(f"\nAnalyzing {doc.metadata['source']}...")
        response = chain.invoke({"source": doc.metadata['source'], "content": doc.page_content[:3000]}) # Truncate for safety
        print(response.content)

if __name__ == "__main__":
    docs = fetch_repo_files(TARGET_REPO, TARGET_PATH)
    if docs:
        analyze_code(docs)
