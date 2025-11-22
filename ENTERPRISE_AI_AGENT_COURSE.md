# ANTIGRAVITY AGENT TASK SPECIFICATION
# Enterprise AI Agent Development: From RAG to Risk Assessment

---

## 🎯 INITIAL PROMPT FOR ANTIGRAVITY

**Model Configuration**: Gemini 3 Pro (High thinking level) | Planning Mode enabled

**Copy this prompt to Antigravity Agent Manager**:

```
# ROLE
You are a technical curriculum architect building a production-grade AI agent development course.

# OBJECTIVE
Create complete course implementation: 6-8 modules teaching LangChain, vector RAG, LangSmith, MCP servers, multi-agent orchestration, Markov Chains, and Judge Agents. Final deliverable is enterprise risk assessment system.

# CONTEXT
Learner: Technical professional with Python experience
Goal: Master sophisticated agentic systems for automation and analytical breakthroughs
Output: 4 portfolio-ready projects demonstrating production capabilities

# REQUIRED DELIVERABLES

## Phase 1: Architecture & Foundation (FIRST)
1. Propose 6-8 module structure with clear progression
2. Create GEMINI.md context file with:
   - Course architecture decisions
   - Dependency versions (langchain>=0.3.9, langgraph>=0.2.53, crewai>=0.86.0, pinecone-client>=5.0.0, mcp>=1.0.0)
   - Standard patterns and templates
   - Lab validation criteria
3. Generate project structure (directories, .gitignore, requirements.txt)
4. Create validate_environment.py with pre-flight checks
5. Produce Implementation Plan artifact for review

## Phase 2: Module 1 Complete Implementation
After Phase 1 approval, build Module 1 with:
- Standard lab template (logging, error handling, Pydantic schemas, LangSmith integration)
- Working code examples for all concepts
- Test coverage ≥70%
- README with learning objectives and validation criteria
- Knowledge check questions

## Phase 3: Parallel Module Development
Spawn separate agents for Modules 2-4:
- Agent 1: Module 2 (Vector RAG + Pinecone)
- Agent 2: Module 3 (LangSmith observability)  
- Agent 3: Module 4 (MCP server development)

## Phase 4: Advanced Modules + Capstone
Sequential implementation:
- Modules 5-8 (LangGraph, CrewAI, Judge Agents, Markov Chains)
- Final capstone: Enterprise Risk Assessment System

# CONSTRAINTS
- Type hints throughout, no print() statements (use logging)
- Pydantic for all structured outputs
- Pre-flight validation in every lab
- LangSmith tracing integrated from Module 1
- No hardcoded credentials
- Portfolio-quality code and documentation

# EXECUTION INSTRUCTIONS
1. Review full course specification in this document
2. Generate Phase 1 deliverables as artifacts
3. Request review before proceeding to Phase 2
4. Update GEMINI.md after each session with learnings and progress
5. Use @ symbol to reference files: @validate_environment.py, @requirements.txt
6. Create Walkthrough Artifacts with browser testing for interactive components

# OUTPUT FORMAT
Start with Implementation Plan artifact showing:
- Proposed module structure
- Key architectural decisions
- Dependencies and versions
- Timeline estimate
- Any questions requiring clarification

DO NOT implement code until Implementation Plan is reviewed and approved.
```

**After pasting prompt**:
1. Review the Implementation Plan artifact Antigravity generates
2. Approve or provide feedback
3. Type "Proceed with Phase 1" to begin implementation
4. Monitor Agent Manager Inbox for progress updates

---

## 📋 COURSE OVERVIEW

**Target Learner**: Technical professional with Python experience seeking to master sophisticated agentic systems for solving complex problems, driving automation, and building breakthrough analytical capabilities

**Duration**: 6-8 modules, 40-60 hours total

**Tech Stack**: LangChain, LangGraph, CrewAI, Pinecone, MCP, Anthropic/OpenAI APIs, LangSmith

**Portfolio Goal**: 4 production-ready projects demonstrating RAG, multi-agent orchestration, observability, and advanced reasoning patterns

---

## 🎓 REQUIRED LEARNING OUTCOMES

### Core Competencies
1. **Vector RAG Systems**: Build production retrieval-augmented generation with semantic search, hybrid ranking, and context management
2. **Multi-Agent Orchestration**: Design coordinated agent systems using LangGraph state machines and CrewAI hierarchies
3. **Observability**: Implement comprehensive tracing, logging, and debugging with LangSmith
4. **Custom Tools & MCP**: Create reusable tools and Model Context Protocol servers for external integrations
5. **Probabilistic Reasoning**: Apply Markov Chains for scenario generation and risk modeling
6. **Quality Control**: Implement Judge Agent patterns with evaluation frameworks

### Domain Applications
- Security control discovery from documentation
- Threat scenario generation with MITRE ATT&CK
- Risk scoring through multi-agent evaluation
- Compliance document analysis
- Automated security assessments

---

## 🏗️ SUGGESTED MODULE STRUCTURE

### Module 1: LangChain Foundations & Tool Creation (6-8 hrs)
**Concepts**: Chains, prompts, output parsers, function calling, custom tools
**Labs**:
1. Build basic chain with prompt templates and output parsing
2. Create custom Python tools with error handling
3. Implement function calling for structured outputs
4. Build tool executor with retry logic

**Deliverable**: Reusable tool library for security APIs (NVD, CISA KEV, MITRE ATT&CK)

---

### Module 2: Vector Databases & RAG Systems (8-10 hrs)
**Concepts**: Embeddings, semantic search, Pinecone, hybrid retrieval, context management
**Labs**:
1. Set up Pinecone and create vector indexes
2. Implement document chunking strategies
3. Build semantic search with metadata filtering
4. Create hybrid search (semantic + keyword)
5. Implement RAG pipeline with context window management

**Deliverable**: Compliance document RAG system that retrieves relevant controls and policies

**Technical Requirements**:
- Pinecone vector database
- Embedding models (OpenAI or sentence-transformers)
- Document loaders for PDF/DOCX
- Chunking strategies (semantic, fixed-size, recursive)
- Metadata filtering and namespaces

---

### Module 3: LangSmith Observability & Debugging (4-6 hrs)
**Concepts**: Tracing, evaluation, dataset management, debugging workflows
**Labs**:
1. Set up LangSmith project and tracing
2. Implement custom trace metadata
3. Create evaluation datasets
4. Build automated quality metrics
5. Debug complex agent failures using trace analysis

**Deliverable**: Comprehensive monitoring framework for all subsequent projects

**Key Patterns**:
- Trace annotations for cost tracking
- Custom evaluators for domain-specific metrics
- Dataset versioning for regression testing
- Error pattern analysis

---

### Module 4: Model Context Protocol (MCP) Development (6-8 hrs)
**Concepts**: MCP servers, resource providers, tool schemas, client integration
**Labs**:
1. Build MCP server for ServiceNow integration
2. Create MCP server for local file operations
3. Implement MCP resource provider for security feeds
4. Build custom MCP client for agent workflows
5. Test MCP servers with Claude Desktop/Antigravity

**Deliverable**: 3 production MCP servers (ServiceNow, SecurityFeeds, FileOps)

**MCP Server Examples**:
```python
# ServiceNow MCP Server
- Tools: query_incidents, get_cmdb_items, search_knowledge
- Resources: incident_templates, priority_matrix

# Security Feeds MCP Server  
- Tools: query_nvd, get_cisa_kev, search_mitre_attack
- Resources: threat_intel_feeds, vulnerability_database

# FileOps MCP Server
- Tools: read_policy_doc, extract_controls, parse_audit_findings
- Resources: compliance_frameworks, control_catalog
```

---

### Module 5: LangGraph & Multi-Agent Orchestration (10-12 hrs)
**Concepts**: StateGraph, conditional routing, cycles, parallel execution, checkpoints
**Labs**:
1. Build stateful workflow with TypedDict state
2. Implement conditional routing based on LLM decisions
3. Create reflection loops with max iterations
4. Design parallel agent execution
5. Implement checkpointing for long-running workflows

**Deliverable**: Self-correcting document analysis workflow (analyze → critique → refine)

**State Management Patterns**:
- Separate channels for messages, context, results, errors
- State reducers for list aggregation
- Checkpoint strategies for resume/replay
- Error recovery and graceful degradation

---

### Module 6: CrewAI & Hierarchical Teams (8-10 hrs)
**Concepts**: Roles, tasks, processes, delegation, Pydantic outputs, custom tools
**Labs**:
1. Build sequential crew for research workflow
2. Implement hierarchical crew with manager delegation
3. Create Pydantic output schemas for structured results
4. Integrate custom tools and MCP servers
5. Build crew with conditional task routing

**Deliverable**: Security assessment crew (Analyst → Validator → Reporter)

**Crew Architectures**:
- Sequential: Linear task flow with context passing
- Hierarchical: Manager delegates to specialist agents
- Conditional: Dynamic task routing based on results

---

### Module 7: Judge Agent Pattern & Quality Control (6-8 hrs)
**Concepts**: Evaluation criteria, Pydantic schemas, conditional routing, multi-criteria scoring
**Labs**:
1. Design Judge Agent with evaluation rubric
2. Implement Pydantic evaluation schema
3. Build Worker → Judge → Router pattern
4. Create multi-criteria judge with weighted scoring
5. Integrate Judge into CrewAI workflows

**Deliverable**: Quality gate system for security documentation validation

**Judge Agent Patterns**:
```python
class SecurityEvaluation(BaseModel):
    completeness: bool = Field(description="All controls identified")
    accuracy: bool = Field(description="No false positives")
    relevance: bool = Field(description="Findings match scope")
    severity_correct: bool = Field(description="Risk ratings appropriate")
    overall_pass: bool = Field(description="Meets quality threshold")
    score: float = Field(ge=0.0, le=1.0)
    feedback: str = Field(description="Specific improvements needed")
```

---

### Module 8: Markov Chains & Probabilistic Reasoning (8-10 hrs)
**Concepts**: State transitions, probability matrices, scenario generation, MITRE ATT&CK integration
**Labs**:
1. Build basic Markov Chain for threat progression
2. Implement MITRE ATT&CK technique transitions
3. Create scenario generator using transition probabilities
4. Integrate with LangChain for narrative generation
5. Build attack path probability calculator

**Deliverable**: Threat scenario generator using Markov Chains with MITRE ATT&CK

**Markov Chain Applications**:
```python
# Attack progression model
States: [Reconnaissance, Initial Access, Persistence, Privilege Escalation, 
         Lateral Movement, Collection, Exfiltration]

# Transition probabilities from historical data
P(Persistence | Initial Access) = 0.85
P(Lateral Movement | Privilege Escalation) = 0.72

# Generate realistic attack scenarios
# Integrate with MITRE ATT&CK technique taxonomy
# Use LLM to create narrative from state sequence
```

---

## 🎯 FINAL CAPSTONE PROJECT

### Enterprise Risk Assessment System (15-20 hrs)

**System Architecture**:
```
Data Ingestion Layer
├── ServiceNow MCP (incidents, CMDB)
├── Security Feeds MCP (NVD, CISA, MITRE)
└── Document RAG (policies, audit findings)

Analysis Layer (CrewAI Hierarchical Crew)
├── Control Discovery Agent → RAG system for existing controls
├── Threat Modeling Agent → Markov Chain scenario generation
├── Vulnerability Analyst → API integration for CVE enrichment
└── Risk Scoring Agent → Multi-framework evaluation (FAIR, NIST)

Quality Control Layer (LangGraph)
├── Judge Agent → Validates completeness, accuracy, consistency
├── Router → Routes to refinement or approval
└── Report Generator → Creates final risk assessment

Orchestration Layer (LangGraph StateGraph)
├── Parallel ingestion from multiple sources
├── Sequential analysis through CrewAI
├── Conditional quality checks
└── Iterative refinement until approval
```

**Components**:

1. **Control Discovery Agent**
   - Uses RAG to search compliance docs
   - Extracts existing controls
   - Maps to frameworks (NIST CSF, ISO 27001)

2. **Threat Modeling Agent**
   - Generates scenarios using Markov Chains
   - Integrates MITRE ATT&CK techniques
   - Produces attack narratives

3. **Vulnerability Analyst**
   - Queries NVD via MCP
   - Enriches CVE data
   - Prioritizes based on exploitability

4. **Risk Scoring Agent**
   - Applies FAIR methodology
   - Uses Tree of Thought for complex scoring
   - Considers multiple evaluation frameworks

5. **Judge Agent**
   - Multi-criteria evaluation
   - Validates methodology application
   - Checks for completeness and accuracy

**Technical Stack**:
- LangGraph for workflow orchestration
- CrewAI for hierarchical analysis team
- Pinecone for control/policy RAG
- MCP servers for ServiceNow, NVD, MITRE ATT&CK
- Markov Chains for threat modeling
- LangSmith for comprehensive tracing

**Deliverables**:
- Functional multi-agent system
- Comprehensive documentation
- Architecture diagrams
- Performance analysis
- Test coverage 80%+
- Portfolio presentation materials

---

## 💻 TECHNICAL REQUIREMENTS

### Core Dependencies
```python
# LangChain ecosystem
langchain >= 0.3.9
langchain-community >= 0.3.9
langchain-core >= 0.3.19
langgraph >= 0.2.53
langsmith >= 0.1.147

# Multi-agent frameworks
crewai >= 0.86.0
crewai-tools >= 0.17.0

# Vector database
pinecone-client >= 5.0.0

# MCP
mcp >= 1.0.0  # or fastmcp for Python
anthropic-mcp-client >= 0.1.0

# LLM providers
langchain-anthropic >= 0.3.3
langchain-openai >= 0.2.12

# Data & utilities
pydantic >= 2.10.3
numpy >= 1.26.0  # for Markov Chains
networkx >= 3.0  # for graph-based modeling
python-dotenv >= 1.0.1

# Testing & quality
pytest >= 8.3.4
pytest-asyncio >= 0.24.0
pytest-cov >= 6.0.0
```

### API Keys Required
```bash
# LLM Providers (at least one)
ANTHROPIC_API_KEY=
OPENAI_API_KEY=

# Vector Database
PINECONE_API_KEY=
PINECONE_ENVIRONMENT=

# Observability
LANGCHAIN_API_KEY=
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=enterprise-risk-assessment

# Security APIs (optional but recommended)
NVD_API_KEY=
SERVICENOW_INSTANCE=
SERVICENOW_USERNAME=
SERVICENOW_PASSWORD=
```

---

## 📐 CORE PATTERNS & TEMPLATES

### Standard Lab Structure
```python
"""
Module X Lab Y: [Name]
Objective: [One sentence]
Concepts: [Key learnings]
"""
import os
import logging
from typing import TypedDict, List, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Configure
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
load_dotenv()

# Pre-flight validation
def validate_environment(required_keys: List[str]) -> None:
    """Verify environment setup"""
    missing = [k for k in required_keys if not os.getenv(k)]
    if missing:
        raise EnvironmentError(f"Missing: {', '.join(missing)}")
    logger.info("✅ Environment validated")

# Pydantic models for structured outputs
class LabOutput(BaseModel):
    """Define expected output structure"""
    pass  # Customize per lab

# Main implementation
def main():
    """Execute lab"""
    try:
        validate_environment(["ANTHROPIC_API_KEY"])
        
        # Lab implementation
        
        logger.info("✅ Lab completed successfully")
        
    except Exception as e:
        logger.error(f"❌ Lab failed: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
```

### LangSmith Integration Pattern
```python
from langsmith import Client
from langsmith.run_helpers import traceable

client = Client()

@traceable(
    run_type="chain",
    name="custom_operation",
    project_name="enterprise-risk-assessment"
)
def tracked_function(inputs: dict) -> dict:
    """All function calls automatically traced"""
    # Implementation
    return outputs

# Custom metadata
@traceable(metadata={"cost_center": "security", "priority": "high"})
def expensive_operation(data):
    pass
```

### MCP Server Template
```python
"""
MCP Server: [Name]
Provides: [Tools/Resources]
"""
from mcp.server import Server
from mcp.types import Tool, Resource
import asyncio

server = Server("server-name")

@server.tool()
async def custom_tool(param: str) -> dict:
    """
    Tool description for LLM
    
    Args:
        param: Parameter description
    
    Returns:
        Structured result
    """
    # Implementation
    return {"result": "data"}

@server.resource("resource://type/path")
async def custom_resource() -> str:
    """Provide resource data"""
    return "resource content"

if __name__ == "__main__":
    asyncio.run(server.run())
```

### Markov Chain Template
```python
import numpy as np
from typing import Dict, List

class ThreatMarkovChain:
    """Generate attack scenarios using Markov Chains"""
    
    def __init__(self, transition_matrix: np.ndarray, states: List[str]):
        self.transitions = transition_matrix
        self.states = states
        self.state_to_idx = {s: i for i, s in enumerate(states)}
    
    def generate_scenario(
        self, 
        start_state: str, 
        max_steps: int = 10
    ) -> List[str]:
        """Generate attack progression sequence"""
        current_idx = self.state_to_idx[start_state]
        scenario = [start_state]
        
        for _ in range(max_steps):
            # Sample next state from transition probabilities
            probs = self.transitions[current_idx]
            next_idx = np.random.choice(len(self.states), p=probs)
            
            # Terminal state check
            if probs[next_idx] == 0:
                break
                
            scenario.append(self.states[next_idx])
            current_idx = next_idx
        
        return scenario
    
    def scenario_probability(self, sequence: List[str]) -> float:
        """Calculate probability of scenario"""
        prob = 1.0
        for i in range(len(sequence) - 1):
            current = self.state_to_idx[sequence[i]]
            next_state = self.state_to_idx[sequence[i + 1]]
            prob *= self.transitions[current][next_state]
        return prob

# MITRE ATT&CK integration
MITRE_ATTACK_TRANSITIONS = {
    "T1595": {"T1190": 0.65, "T1566": 0.35},  # Reconnaissance -> Initial Access
    "T1190": {"T1053": 0.50, "T1136": 0.30, "T1078": 0.20},  # Exploit -> Persistence
    # ... build from historical attack data
}
```

### Judge Agent Pattern
```python
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class Evaluation(BaseModel):
    """Standard evaluation schema"""
    criteria_met: Dict[str, bool] = Field(description="Individual criteria")
    overall_pass: bool = Field(description="Pass/fail decision")
    score: float = Field(ge=0.0, le=1.0, description="Quality score")
    feedback: str = Field(description="Detailed improvement guidance")

def create_judge_agent(evaluation_criteria: Dict[str, str]) -> Any:
    """Factory for Judge Agents"""
    
    criteria_prompt = "\n".join([
        f"- {name}: {description}" 
        for name, description in evaluation_criteria.items()
    ])
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a quality evaluator. Assess the provided output against these criteria:
        
{criteria_prompt}

Provide structured evaluation."""),
        ("user", "Evaluate this output:\n\n{output}")
    ])
    
    llm = ChatAnthropic(model="claude-sonnet-4-20250514")
    
    return prompt | llm.with_structured_output(Evaluation)
```

---

## ✅ VALIDATION CRITERIA

### Per-Module Requirements
- [ ] All labs executable without errors
- [ ] Code follows quality standards (types, logging, error handling)
- [ ] Pydantic models for structured data
- [ ] LangSmith tracing integrated
- [ ] Tests with 70%+ coverage
- [ ] Documentation with examples
- [ ] Knowledge checks answered

### Project Requirements
- [ ] All 4 portfolio projects completed
- [ ] Comprehensive README for each
- [ ] Architecture diagrams included
- [ ] Performance metrics documented
- [ ] GitHub repository public
- [ ] Demo video or screenshots
- [ ] Resume bullets drafted

### Code Quality Standards
- Type hints throughout
- Comprehensive error handling
- Structured logging (not print)
- Environment validation
- Configuration externalized
- No hardcoded secrets
- DRY principles
- Clear documentation

---

## 🎯 PORTFOLIO PROJECTS

### Project 1: Compliance RAG System (Module 2)
**Tech**: LangChain, Pinecone, document loaders
**Function**: Search compliance documents, retrieve relevant controls
**Metrics**: Retrieval accuracy, latency, context relevance

### Project 2: MCP Integration Suite (Module 4)
**Tech**: MCP protocol, custom servers, client integration
**Function**: 3 production MCP servers for security APIs
**Metrics**: Tool success rate, error handling, response time

### Project 3: Self-Correcting Analysis Workflow (Modules 5-7)
**Tech**: LangGraph, CrewAI, Judge Agents
**Function**: Document analysis with reflection and refinement
**Metrics**: Approval rate, iteration count, quality improvement

### Project 4: Enterprise Risk Assessment Platform (Module 8 + Capstone)
**Tech**: Full stack integration
**Function**: Multi-source ingestion → analysis → risk scoring → validation
**Metrics**: Scenario quality, risk score accuracy, system throughput

---

## 📊 SUCCESS METRICS

### Learning Outcomes
- Explain RAG architecture and optimization strategies
- Design multi-agent workflows with state management
- Debug complex agent systems using traces
- Build MCP servers for custom integrations
- Apply Markov Chains to domain problems
- Implement quality control patterns

### Technical Achievements
- 4 portfolio-ready projects deployed
- 80%+ test coverage on capstone
- Comprehensive documentation
- Performance benchmarks documented
- Cost analysis completed
- Security best practices applied

### Career Readiness
- Resume bullets quantified
- GitHub profile showcases work
- Can explain architectural decisions
- Prepared for technical interviews
- Portfolio website ready
- LinkedIn updated with projects

---

## 🚀 EXECUTION GUIDANCE

### Phase 1: Foundation (Modules 1-3)
Build core capabilities:
- LangChain proficiency
- RAG system implementation
- Observability patterns
- Tool creation skills

### Phase 2: Integration (Modules 4-5)
Expand connectivity:
- MCP server development
- State machine workflows
- Multi-agent coordination
- Complex error handling

### Phase 3: Advanced Patterns (Modules 6-7)
Master orchestration:
- Hierarchical teams
- Quality control
- Evaluation frameworks
- Self-correction

### Phase 4: Domain Application (Module 8 + Capstone)
Apply to risk assessment:
- Probabilistic modeling
- Threat scenario generation
- Full system integration
- Production deployment

---

## ⚡ CRITICAL SUCCESS STRATEGIES

### Rate Limit Management
Antigravity refreshes credits every 5 hours. Plan intensive work accordingly:
- **High-credit sessions**: Phase 3 parallel agent spawning, complex implementations, browser testing
- **Low-credit sessions**: Artifact reviews, documentation, git commits, planning
- **Key insight**: Agents continue working even if you hit limits mid-task. Monitor Agent Manager Inbox for completion notifications.

### Portfolio Attribution Strategy
When agents generate most code, articulate YOUR contribution clearly:

**Effective resume bullets**:
```
✅ "Architected 8-module AI agent course integrating RAG, MCP, and Markov Chains for enterprise risk assessment"
✅ "Designed Judge Agent evaluation framework achieving 85% approval rate through multi-criteria Pydantic schemas"
✅ "Orchestrated 4 parallel agents reducing 30-day development timeline to 6 days through asynchronous workflows"
```

**What matters to employers**:
- Architectural decisions you made
- Orchestration strategies you designed
- Problems you solved through agent delegation
- NOT: Lines of code typed

### Discovery-First Validation Protocol
Based on real-world agent fabrication patterns, implement verification gates:

```markdown
## Validation Protocol (Add to every module README)

1. **Implementation Plan Review**: Agent generates plan artifact → Review BEFORE execution approval
2. **Artifact Verification**: Check /mnt/user-data/outputs for actual files, not just completion messages
3. **Browser Validation**: Confirm screenshots and recordings match stated requirements
4. **Git Verification**: Run `git status` and `git diff` to verify actual file changes
5. **Execution Testing**: Run validate_environment.py, execute labs independently

CRITICAL: Never trust "completion" announcements without artifact verification.
```

Antigravity's artifact system (Implementation Plans, Browser Recordings, Code Diffs) provides proof of work—use it.

### Security Considerations for Preview
Current security limitations require defensive practices:

**During public preview**:
- Use synthetic/mock data for ServiceNow integrations
- Generate fake MITRE ATT&CK scenarios, not real threat intelligence
- Avoid processing actual vulnerability data or audit findings
- Create realistic-looking test data for portfolio demonstrations

**Document clearly**:
```
"Note: Demo uses synthetic security data. Production deployment requires 
enterprise Antigravity license with appropriate security controls."
```

Wait for enterprise release before processing sensitive organizational data.

---

## 💡 IMPLEMENTATION FLEXIBILITY

### You Decide:
- Exact module count (6-8 recommended)
- Lab sequence within modules
- Specific implementation details
- Directory structure
- Testing frameworks
- Additional utilities

### Must Maintain:
- Pydantic for structured outputs
- LangSmith integration throughout
- Pre-flight validation pattern
- Error handling standards
- Documentation requirements
- Portfolio quality

### Optimize For:
- Learning progression (simple → complex)
- Reusable patterns across labs
- Clear debugging when failures occur
- Portfolio showcase quality
- Real-world applicability

---

## 📝 DOCUMENTATION STANDARDS

### Code Documentation
- Docstrings for all functions (Google style)
- Type hints throughout
- Inline comments for complex logic
- README per module

### Project Documentation
- Architecture diagrams (Mermaid or similar)
- Setup instructions
- Usage examples
- Performance analysis
- Lessons learned

### Portfolio Materials
- Executive summary (what problem solved)
- Technical highlights
- Quantitative results
- Code samples
- Demo video or screenshots

---

## 🎓 KNOWLEDGE VERIFICATION

### Core Concepts to Master
1. **RAG Systems**: When to use semantic vs hybrid search, chunking strategies, context management
2. **LangGraph**: State management, conditional routing, checkpoint strategies, error recovery
3. **MCP**: Server vs client architecture, tool schemas, resource providers, integration patterns
4. **Markov Chains**: Transition matrices, scenario generation, probability calculations, MITRE integration
5. **Judge Agents**: Evaluation criteria design, Pydantic schemas, routing logic, bias prevention

### Can You Explain:
- Trade-offs between CrewAI and LangGraph
- When to use vector search vs keyword search
- How to debug multi-agent failures
- How Markov Chains generate scenarios
- How Judge Agents prevent bias
- When to create MCP servers vs custom tools

---

## 🚦 READY TO BUILD

**Your Implementation Plan Should Include**:
1. Proposed module structure (6-8 modules)
2. Lab breakdown per module
3. Progression of complexity
4. Integration points between modules
5. Capstone project architecture

**Execute Phase 1**:
- Project structure setup
- Environment validation scripts
- Standard templates creation
- Module 1 implementation with working examples
- Progress tracking system

**Then Report**:
- What's completed
- What's next
- Any blockers or questions
- Estimated timeline for remaining work

**Remember**: This spec provides constraints and patterns, not a rigid script. Make good architectural decisions that serve the learning objectives and produce portfolio-worthy code.

**Your move, Antigravity. Build something exceptional.**
