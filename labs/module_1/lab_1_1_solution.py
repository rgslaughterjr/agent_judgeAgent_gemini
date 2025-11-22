import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

# Note: Ensure OPENAI_API_KEY and LANGSMITH_API_KEY are set in your environment
# os.environ["OPENAI_API_KEY"] = "sk-..."
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = "ls-..."

def run_lab_1_1():
    print("### Lab 1.1: Security Researcher (CrewAI + LangSmith) ###")
    print("Goal: Research a specific NIST AI RMF function and summarize it.")

    # 1. Define Agents
    # The Researcher: Specialist in NIST standards
    nist_analyst = Agent(
        role='NIST AI RMF Analyst',
        goal='Analyze the NIST AI Risk Management Framework (AI RMF) to understand specific functions and controls.',
        backstory="""You are a senior cybersecurity compliance analyst specializing in AI risk. 
        You have deep knowledge of NIST standards. Your job is to explain complex control requirements clearly.""",
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(model_name="gpt-4o", temperature=0) # Or gpt-3.5-turbo
    )

    # The Writer: Communicates to executives
    compliance_writer = Agent(
        role='Executive Compliance Writer',
        goal='Summarize technical risk analysis into executive-level briefs.',
        backstory="""You are a technical writer who specializes in communicating risk to the C-suite. 
        You take technical jargon and turn it into actionable business intelligence.""",
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(model_name="gpt-4o", temperature=0.7)
    )

    # 2. Define Tasks
    # Task 1: Research the 'GOVERN' function
    research_task = Task(
        description="""Research the 'GOVERN' function of the NIST AI RMF 1.0. 
        Identify its primary purpose, key categories (e.g., GOVERN 1.1), and why it is foundational for AI safety.
        Use your internal knowledge or search tools if available (using internal knowledge for this basic lab).""",
        expected_output="""A detailed bulleted list of the GOVERN function's objectives and at least 3 key sub-categories with descriptions.""",
        agent=nist_analyst
    )

    # Task 2: Write the brief
    write_task = Task(
        description="""Using the analyst's research, write a 1-paragraph executive summary on why the GOVERN function is critical for our organization's AI strategy. 
        Tone should be professional, urgent, and strategic.""",
        expected_output="""A professional executive summary paragraph.""",
        agent=compliance_writer
    )

    # 3. Instantiate Crew
    crew = Crew(
        agents=[nist_analyst, compliance_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True
    )

    # 4. Kickoff
    result = crew.kickoff()

    print("\n\n########################")
    print("## Final Crew Output ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    # Check for keys (Optional simple check)
    if not os.environ.get("OPENAI_API_KEY"):
        print("WARNING: OPENAI_API_KEY not found in environment. The agents may fail if not configured.")
    
    run_lab_1_1()
