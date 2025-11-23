# Agent Judge - AI Agent Development Labs

A comprehensive learning project focused on building AI agents using LangChain, LangGraph, and modern AI frameworks. This repository contains hands-on labs covering agent workflows, RAG systems, and code security analysis.

## 🎯 Project Overview

This project demonstrates practical implementations of AI agent concepts including:

- **Stateful Workflows** with LangGraph
- **Retrieval Augmented Generation (RAG)** with Pinecone
- **Code Security Analysis** using GitHub API
- **PII Detection & Routing** for compliance

## 🛠️ Tech Stack

- **LangChain** - Agent framework and document processing
- **LangGraph** - Stateful agent workflows
- **OpenAI GPT-4** - Language model for analysis
- **Pinecone** - Vector database for RAG
- **PyGithub** - GitHub API integration
- **Python 3.11+** - Core language

## 📚 Labs

### Module 1: Fundamentals

#### Lab 1.1: Security Researcher

- **Concepts**: LangGraph state management, sequential workflows
- **Implementation**: Multi-agent system for NIST AI RMF analysis
- **File**: [`labs/module_1/lab_1_1_starter.py`](labs/module_1/lab_1_1_starter.py)

#### Lab 1.2: PII Router

- **Concepts**: Conditional routing, state-based decisions
- **Implementation**: PII detection and redaction workflow
- **File**: [`labs/module_1/lab_1_2_starter.py`](labs/module_1/lab_1_2_starter.py)

#### Lab 1.3: Advanced RAG

- **Concepts**: Vector embeddings, multi-query retrieval
- **Implementation**: Policy document search with Pinecone
- **File**: [`labs/module_1/lab_1_3_starter.py`](labs/module_1/lab_1_3_starter.py)

#### Lab 1.4: Code Inspector

- **Concepts**: GitHub API, automated security analysis
- **Implementation**: Repository scanning for hardcoded secrets
- **File**: [`labs/module_1/lab_1_4_starter.py`](labs/module_1/lab_1_4_starter.py)

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Pinecone API key (for Lab 1.3)
- GitHub token (for Lab 1.4)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/rgslaughterjr/agent_judgeAgent_gemini.git
   cd agent_judgeAgent_gemini
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:

   ```bash
   OPENAI_API_KEY=your_openai_key_here
   PINECONE_API_KEY=your_pinecone_key_here
   GITHUB_TOKEN=your_github_token_here
   ```

### Running Labs

Each lab can be run independently:

```bash
# Lab 1.1: Security Researcher
python labs/module_1/lab_1_1_starter.py

# Lab 1.2: PII Router
python labs/module_1/lab_1_2_starter.py

# Lab 1.3: Advanced RAG
python labs/module_1/lab_1_3_starter.py

# Lab 1.4: Code Inspector
python labs/module_1/lab_1_4_starter.py
```

## 📖 Key Learnings

### LangGraph Patterns

- State management with `TypedDict`
- Conditional routing for dynamic workflows
- Node-based agent architecture

### RAG Implementation

- Document chunking strategies
- Vector embeddings with OpenAI
- Multi-query retrieval for better results

### Security Analysis

- Automated code scanning
- LLM-based vulnerability detection
- GitHub API integration patterns

## 🔒 Security Notes

- Never commit `.env` files (already in `.gitignore`)
- Use environment variables for all API keys
- Rotate tokens regularly
- Review AI-generated code before production use

## 📝 Project Structure

```
agent_judgeAgent_gemini/
├── labs/
│   └── module_1/
│       ├── lab_1_1_starter.py    # Security Researcher
│       ├── lab_1_2_starter.py    # PII Router
│       ├── lab_1_3_starter.py    # Advanced RAG
│       └── lab_1_4_starter.py    # Code Inspector
├── data/
│   ├── internal_ai_policy.txt    # Sample policy document
│   └── nist_rmf_gov.md          # NIST framework guide
├── .env                          # Environment variables (not in repo)
├── .gitignore
└── README.md
```

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Guide](https://langchain-ai.github.io/langgraph/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Pinecone Documentation](https://docs.pinecone.io/)

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is for educational purposes.

## 👤 Author

**Richard Slaughter Jr.**

- GitHub: [@rgslaughterjr](https://github.com/rgslaughterjr)
- Focus: AI Agent Development, Cybersecurity, Enterprise Risk Assessment

---

*Built as part of an AI Agent Development learning path, focusing on practical implementations of LangChain and LangGraph for enterprise AI applications.*
