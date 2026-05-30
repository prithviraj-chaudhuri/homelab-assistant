import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
from deepagents import create_deep_agent
from langfuse import observe
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from agents import research_agent

langfuse = get_client()
langfuse.flush()

langfuse_handler = CallbackHandler()

root = Path(__file__).resolve().parent
research_skill_path = root / "skills" / "research" / "SKILL.md"
research_skill_text = research_skill_path.read_text(encoding="utf-8") if research_skill_path.exists() else ""

agent = create_deep_agent(
    model=f"openai:{os.getenv('OPENAI_MODEL')}",
    system_prompt=(
        "You are homelab assistant. Your goal is to work with the user and improve their homelab setup. "
        "You have access to subagents that can perform research, analysis, and other tasks to help you achieve your goal. "
        "Refer to your skills and subagents when necessary to accomplish your tasks. Always think step by step and use your subagents when you need to perform specific tasks."
    ),
    skills=[research_skill_text],
    subagents=[research_agent]
)

agent = agent.with_config({"callbacks": [langfuse_handler]})
