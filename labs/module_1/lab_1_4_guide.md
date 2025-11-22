# Lab 1.4: Code Inspector (GitHub API + LangChain)

## Goal

Learn how to build an agent capability that can **read and analyze external code repositories**. This is essential for a "Judge Agent" that needs to audit other agents' code for security flaws or policy violations.

## Concepts

### 1. GitHub API

To inspect code programmatically, we use the GitHub API.

* **Authentication**: You need a `GITHUB_TOKEN` to avoid rate limits and access private repos.
* **Structure**: Repositories contain Files (Blobs) and Directories (Trees).

### 2. LangChain Document Loaders

LangChain provides loaders to simplify fetching data.

* `GithubFileLoader`: Fetches specific files.
* `GitLoader`: Clones a repo locally and loads files (good for deep analysis).
* *In this lab, we will use a custom approach using the `PyGithub` library or raw API requests to fetch file content, then wrap it in LangChain `Document` objects.*

### 3. Static Analysis (Basic)

Once you have the code as text, you can use an LLM to perform static analysis:

* "Does this code use `eval()`?"
* "Is there a hardcoded API key?"
* "Does it import prohibited libraries?"

## Instructions

1. **Open `lab_1_4_starter.py`**.
2. **Step 1**: Setup your GitHub Token (optional for public repos, but recommended).
3. **Step 2**: Implement `fetch_repo_content()`. Use the `github` library (PyGithub) to get the contents of a target repo (e.g., a sample agent repo).
4. **Step 3**: Convert the files into LangChain `Document` objects.
5. **Step 4**: Create a simple analysis chain using an LLM to check for "hardcoded secrets" in the code.

## Resources

* [PyGithub Documentation](https://pygithub.readthedocs.io/en/latest/)
* [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
