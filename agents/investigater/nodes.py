import os
from dotenv import load_dotenv
from langchain_core import messages
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage
from agents.researcher.tools import get_tools

load_dotenv()

PLAN_NODE = 'plan'
TOOL_NODE = 'tools'

OPENAI_MODEL = os.getenv('OPENAI_MODEL')
if not OPENAI_MODEL:
    raise RuntimeError(
        'OPENAI_MODEL is not set. Please define it in your environment or .env file before starting the agent.'
    )

model = ChatOpenAI(
    model=OPENAI_MODEL,
    temperature=0)

model = model.bind_tools(get_tools())

SYSTEM_PROMPT = (
    "You are a planner agent designed to analyze user requests and determine when to call tools for understanding the infrastructure or when to conclude with an answer."
    "Your primary function is to decide if a tool call is necessary based on the user's input and to create a clear, actionable plan for the next steps. "
    "Analyze the incoming user request, determine whether a tool call is needed, and provide a concise, actionable plan. "
    "When research is requested, summarize findings clearly and keep the response focused on the specific topic."
)

# Define the Reasoning Node (Agent)
def call_llm_node(state: MessagesState):
    messages = state['messages']
    system_message = SystemMessage(content=SYSTEM_PROMPT)
    response = model.invoke([system_message, *messages])
    return {"messages": [response]}

# Define the Action Node using prebuilt ToolNode
tool_node = ToolNode(get_tools())