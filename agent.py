import os
from dotenv import load_dotenv
from deepagents import create_deep_agent
from langfuse import observe
from langfuse import get_client
from langfuse.langchain import CallbackHandler

load_dotenv()

langfuse = get_client()
langfuse.flush()

langfuse_handler = CallbackHandler() 

agent = create_deep_agent(
    model=f"openai:{os.getenv('OPENAI_MODEL')}",
    system_prompt="You are a research assistant.",
)

agent = agent.with_config({"callbacks": [langfuse_handler]})
