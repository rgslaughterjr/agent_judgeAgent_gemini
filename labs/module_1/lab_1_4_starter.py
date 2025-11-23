import os
from typing import List
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
# You might need to install PyGithub: pip install PyGithub
from github import Github 

# Load environment variables
load_dotenv()

# Target repository - using a smaller example repo for faster testing
TARGET_REPO = "crewAIInc/crewAI-examples"
MAX_FILES = 10  # Limit files to avoid rate limits and long processing

def fetch_repo_files(repo_name: str, max_files: int = MAX_FILES) -> List[Document]:
    """
    Fetch Python files from a GitHub repository.
    
    Args:
        repo_name: Repository in format "owner/repo"
        max_files: Maximum number of files to fetch
        
    Returns:
        List of Document objects containing file content and metadata
    """
    print(f"--- Fetching files from {repo_name} ---")
    
    # 1. Authenticate with GitHub
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("WARNING: No GITHUB_TOKEN found. Using unauthenticated access (rate limited).")
        g = Github()
    else:
        from github import Auth
        auth = Auth.Token(token)
        g = Github(auth=auth)
    
    try:
        # 2. Get the repository object
        repo = g.get_repo(repo_name)
        print(f"    Repository: {repo.full_name}")
        print(f"    Description: {repo.description}")
        
        # 3. Recursively fetch Python files
        docs = []
        contents = repo.get_contents("")
        
        while contents and len(docs) < max_files:
            file_content = contents.pop(0)
            
            # If it's a directory, add its contents to the queue
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            # If it's a Python file, fetch and store it
            elif file_content.name.endswith(".py"):
                try:
                    # Decode the file content
                    code = file_content.decoded_content.decode('utf-8')
                    
                    # Create a LangChain Document
                    doc = Document(
                        page_content=code,
                        metadata={
                            "source": file_content.path,
                            "repo": repo_name,
                            "url": file_content.html_url,
                            "size": file_content.size
                        }
                    )
                    docs.append(doc)
                    print(f"    ✓ Fetched: {file_content.path} ({file_content.size} bytes)")
                    
                except Exception as e:
                    print(f"    ✗ Error fetching {file_content.path}: {e}")
        
        print(f"\n    Total files fetched: {len(docs)}")
        return docs
        
    except Exception as e:
        print(f"    Error accessing repository: {e}")
        return []

def analyze_code(docs: List[Document]):
    """
    Analyze code for security issues using an LLM.
    
    Checks for:
    - Hardcoded secrets (API keys, passwords, tokens)
    - Use of dangerous functions (eval, exec)
    - Prohibited imports
    """
    print("\n--- Analyzing Code for Security Issues ---")
    
    if not docs:
        print("No documents to analyze.")
        return
    
    # 1. Create LLM instance
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    
    # 2. Create analysis prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a security code reviewer. Analyze the provided Python code for security issues.

Focus on:
1. Hardcoded secrets (API keys, passwords, tokens, credentials)
2. Dangerous functions (eval, exec, compile)
3. Suspicious imports (os.system, subprocess with shell=True)

Provide a brief security assessment. If issues are found, list them clearly.
If the code looks safe, say "No major security issues detected."
"""),
        ("user", "File: {filename}\n\nCode:\n{code}")
    ])
    
    # 3. Analyze each file
    chain = prompt | llm
    
    issues_found = []
    
    for i, doc in enumerate(docs, 1):
        filename = doc.metadata.get("source", f"file_{i}")
        print(f"\n[{i}/{len(docs)}] Analyzing: {filename}")
        
        # Truncate very long files to avoid token limits
        code_sample = doc.page_content[:3000]
        if len(doc.page_content) > 3000:
            code_sample += "\n... (truncated)"
        
        try:
            result = chain.invoke({
                "filename": filename,
                "code": code_sample
            })
            
            response = result.content
            print(f"    {response}")
            
            # Track files with issues
            if "No major security issues" not in response:
                issues_found.append({
                    "file": filename,
                    "url": doc.metadata.get("url"),
                    "issues": response
                })
                
        except Exception as e:
            print(f"    Error analyzing: {e}")
    
    # 4. Summary
    print("\n" + "="*60)
    print("SECURITY ANALYSIS SUMMARY")
    print("="*60)
    print(f"Files analyzed: {len(docs)}")
    print(f"Files with potential issues: {len(issues_found)}")
    
    if issues_found:
        print("\nFiles requiring attention:")
        for item in issues_found:
            print(f"  - {item['file']}")
            print(f"    URL: {item['url']}")
    else:
        print("\n✓ No major security issues detected in analyzed files.")

if __name__ == "__main__":
    print("=== Lab 1.4: Code Inspector (GitHub API + LangChain) ===\n")
    
    # 1. Fetch files from repository
    docs = fetch_repo_files(TARGET_REPO, max_files=5)  # Start with just 5 files
    
    # 2. Analyze for security issues
    if docs:
        analyze_code(docs)
    else:
        print("No files were fetched. Check your GitHub token and repository name.")
