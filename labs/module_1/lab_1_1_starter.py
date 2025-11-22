import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Note: Ensure OPENAI_API_KEY is set in your environment

def run_lab_1_1():
    print("### Lab 1.1: Security Researcher (CrewAI) ###")
    print("Goal: Research a specific NIST AI RMF function and summarize it.")

    # --- Step 1: Define Agents ---
    # TODO: Create the NIST Analyst Agent
    # nist_analyst = Agent(
    #     role='...',
    #     goal='...',
    #     backstory='...',
    #     verbose=True,
    #     llm=ChatOpenAI(model_name="gpt-4o", temperature=0)
    # )

    # TODO: Create the Compliance Writer Agent
    # compliance_writer = Agent(...)

    # --- Step 2: Define Tasks ---
    # TODO: Create the Research Task
    # research_task = Task(
    #     description="Research the 'GOVERN' function of NIST AI RMF...",
    #     expected_output="A detailed list of objectives...",
    #     agent=nist_analyst
    # )

    # TODO: Create the Writing Task
    # write_task = Task(...)

    # --- Step 3: Instantiate Crew ---
    # TODO: Create the Crew
    # crew = Crew(
    #     agents=[...],
    #     tasks=[...],
    #     process=Process.sequential,
    #     verbose=True
    # )

    # --- Step 4: Kickoff ---
    print("Starting the Crew...")
    # result = crew.kickoff()
    # print(result)

if __name__ == "__main__":
    run_lab_1_1()
