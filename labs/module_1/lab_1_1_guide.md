# Lab 1.1: Security Researcher (CrewAI)

## Goal

Learn how to orchestrate a team of AI agents using **CrewAI** to perform a multi-step security research task.

## Concepts

### 1. Agents

An **Agent** is an autonomous unit that can perform tasks. It has:

* **Role**: What it is (e.g., "Researcher").
* **Goal**: What it wants to achieve.
* **Backstory**: Context that gives it personality and specific expertise.
* **Tools**: Capabilities it can use (e.g., search, file reading).

### 2. Tasks

A **Task** is a specific assignment for an agent. It has:

* **Description**: Detailed instructions on what to do.
* **Expected Output**: What the result should look like (e.g., "A bulleted list").
* **Agent**: Who is responsible for this task.

### 3. Crew & Process

A **Crew** represents the team. It manages the **Process** (workflow).

* **Sequential Process**: Tasks are executed one after another (Task 1 -> Task 2). The output of Task 1 is passed as context to Task 2.

## Instructions

1. **Open `lab_1_1_starter.py`**.
2. **Step 1**: Define the `nist_analyst` agent. Give it a role like "NIST AI RMF Analyst" and a goal to analyze specific controls.
3. **Step 2**: Define the `compliance_writer` agent. Its goal is to translate technical findings into executive summaries.
4. **Step 3**: Define `research_task`. Ask the analyst to research the "GOVERN" function of NIST AI RMF.
5. **Step 4**: Define `write_task`. Ask the writer to create a brief based on the analyst's findings.
6. **Step 5**: Instantiate the `Crew` with your agents and tasks, and call `kickoff()`.

## Resources

* [CrewAI Documentation](https://docs.crewai.com/)
