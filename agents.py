from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from tools import search_web
from model import openai_model
import logging

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s |%(levelname)s |%(message)s"
)

logging.info("initializing subagent1")
sub_agent1=create_agent(model=openai_model,tools=[search_web],name="subagent1")
logging.info("initializing subagent2")
sub_agent2=create_agent(model=openai_model,tools=[search_web],name="subagent2")

@tool
def delegate_to_subagent1(query : str)->str:
    """search web for a given topic by delegating the task to subagent1"""
    logging.info(f"delegating query to SubAgent1: {query}")
    response= sub_agent1.invoke({"messages":[HumanMessage(content=query)]})
    return response["messages"][-1].content

@tool
def delegate_to_subagent2(query : str)->str:
    """search web for a given topic by delegating the task to subagent2"""
    logging.info(f"delegating query to SubAgent2: {query}")
    response= sub_agent1.invoke({"messages":[HumanMessage(content=query)]})
    return response["messages"][-1].content