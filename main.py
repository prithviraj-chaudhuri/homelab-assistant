import os
from dotenv import load_dotenv
from deepagents import create_deep_agent
from langfuse import observe
from langfuse import get_client
from langfuse.openai import openai

load_dotenv()

langfuse = get_client()
langfuse.flush()

agent = create_deep_agent(
    model=f"openai:{os.getenv('OPENAI_MODEL')}",
    system_prompt="You are a research assistant.",
)
