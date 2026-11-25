from langchain.agents import create_agent
from prompts import WEDDING_PLANNER_AGENT_PROMPT , USER_PROMPT_FOR_MAIN_AGENT
from model import openai_model
from agents import delegate_to_subagent1 , delegate_to_subagent2
from langchain.messages import HumanMessage
import logging

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s |%(levelname)s |%(message)s"
)

logging.info("asking for his requirements")
user_requirements=input("enter the requirements")

updated_system_prompt=WEDDING_PLANNER_AGENT_PROMPT.format(requirements=user_requirements)
logging.info("initializing main agent")
main_agent=create_agent(model=openai_model,tools=[delegate_to_subagent2,delegate_to_subagent1],name="main agent",system_prompt=updated_system_prompt)

logging.info("invoking main agents")
response=main_agent.invoke("messages:" [HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)])
print("main agent response:")
print(response["messages"][-1].content)