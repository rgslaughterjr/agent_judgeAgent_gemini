import os
# pip install pyautogen
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# Ensure OPENAI_API_KEY is set
config_list = [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}]

def run_lab_3_1():
    print("### Lab 3.1: AutoGen Debate ###")
    
    # --- Step 1: Define Agents ---
    # red_agent = AssistantAgent(
    #     name="RedTeam",
    #     system_message="You are a Red Team security expert. Your goal is to find vulnerabilities...",
    #     llm_config={"config_list": config_list}
    # )
    
    # blue_agent = AssistantAgent(...)
    
    # user_proxy = UserProxyAgent(
    #     name="User",
    #     human_input_mode="NEVER",
    #     code_execution_config=False
    # )

    # --- Step 2: Start Chat ---
    # user_proxy.initiate_chat(
    #     red_agent,
    #     message="The system uses MD5 for password hashing."
    # )

if __name__ == "__main__":
    run_lab_3_1()
