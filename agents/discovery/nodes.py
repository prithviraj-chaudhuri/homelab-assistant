import os
from dotenv import load_dotenv
from langchain_core import messages
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage
from agents.discovery.tools import get_tools

load_dotenv()

PLAN_NODE = 'plan'
TOOL_NODE = 'tools'

MODEL_API_KEY = os.getenv('MODEL_API_KEY')
MODEL_MODEL = os.getenv('MODEL_MODEL')
if not MODEL_MODEL:
    raise RuntimeError(
        'MODEL_MODEL is not set. Please define it in your environment or .env file before starting the agent.'
    )

model = ChatOpenAI(
    model=MODEL_MODEL,
    temperature=0,
    openai_api_key=MODEL_API_KEY)

model = model.bind_tools(get_tools())

SYSTEM_PROMPT = (
    "You are a planner agent designed to analyze user requests and determine when to call tools for understanding the infrastructure or when to conclude with an answer."
    "Your primary function is to decide if a tool call is necessary based on the user's input and to create a clear, actionable plan for the next steps. "
    "Analyze the incoming user request, determine whether a tool call is needed, and provide a concise, actionable plan. "
    "When investigation or details about the homelab infrastructure is requested, summarize findings clearly and keep the response focused on the specific topic."
)

# Define the Reasoning Node (Agent)
def call_llm_node(state: MessagesState):
    messages = state['messages']
    system_message = SystemMessage(content=SYSTEM_PROMPT)
    response = model.invoke([system_message, *messages])
    return {"messages": [response]}

# Define the Action Node using prebuilt ToolNode
tool_node = ToolNode(get_tools())