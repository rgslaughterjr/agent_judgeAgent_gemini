import os
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

config_list = [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}]

def run_lab_3_1():
    print("### Lab 3.1: AutoGen Debate (Solution) ###")
    
    # 1. Red Team Agent
    red_agent = AssistantAgent(
        name="RedTeam",
        system_message="You are a Red Team security expert. You aggressively identify vulnerabilities. Be concise and technical.",
        llm_config={"config_list": config_list}
    )
    
    # 2. Blue Team Agent
    blue_agent = AssistantAgent(
        name="BlueTeam",
        system_message="You are a Blue Team security engineer. You propose defenses and mitigations for identified threats. Be constructive.",
        llm_config={"config_list": config_list}
    )
    
    # 3. User Proxy (Triggers the chat)
    user_proxy = UserProxyAgent(
        name="Admin",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=2, # Limit the conversation length
        code_execution_config=False
    )

    # 4. Group Chat (Optional, but good for >2 agents)
    groupchat = GroupChat(agents=[user_proxy, red_agent, blue_agent], messages=[], max_round=4)
    manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})

    # 5. Start
    topic = "We are planning to use a single shared API key for all our microservices."
    print(f"Topic: {topic}")
    
    user_proxy.initiate_chat(
        manager,
        message=topic
    )

if __name__ == "__main__":
    run_lab_3_1()
