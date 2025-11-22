# Lab 3.1: AutoGen Debate (Red vs. Blue)

## Goal

Learn how to use **AutoGen** to create a multi-agent conversation where agents interact autonomously. We will simulate a security debate between a "Red Team" (Attacker) and a "Blue Team" (Defender).

## Concepts

### 1. ConversableAgent

The core class in AutoGen. Agents can send and receive messages.

* **UserProxyAgent**: Represents the user (or a script) that initiates the chat.
* **AssistantAgent**: An LLM-backed agent that follows system instructions.

### 2. GroupChat

A container for multiple agents to talk. A `GroupChatManager` selects the next speaker.

### 3. System Messages

Crucial for defining the "Persona".

* *Red Team*: "You are an aggressive hacker. Find flaws."
* *Blue Team*: "You are a defensive engineer. Propose mitigations."

## Instructions

1. **Open `lab_3_1_starter.py`**.
2. **Step 1**: Define the `config_list` (using your OpenAI key).
3. **Step 2**: Create the `red_agent` and `blue_agent` with distinct system messages.
4. **Step 3**: Create a `moderator` agent to summarize the debate.
5. **Step 4**: Initiate the chat with a topic (e.g., "We are storing passwords in plain text").

## Resources

* [AutoGen Documentation](https://microsoft.github.io/autogen/)
