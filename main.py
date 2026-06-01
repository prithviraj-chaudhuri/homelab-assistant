import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from deepagents import create_deep_agent
from langfuse import observe
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from agents import investigator, research_agent

langfuse = get_client()
langfuse.flush()

langfuse_handler = CallbackHandler()

MODEL_API_KEY = os.getenv('MODEL_API_KEY')
MODEL_MODEL = os.getenv('MODEL_MODEL')
if not MODEL_MODEL:
    raise RuntimeError(
        'MODEL_MODEL is not set. Please define it in your environment or .env file before starting the agent.'
    )
if MODEL_API_KEY:
    os.environ.setdefault('OPENAI_API_KEY', MODEL_API_KEY)

root = Path(__file__).resolve().parent
research_skill_path = root / "skills" / "research" / "SKILL.md"
research_skill_text = research_skill_path.read_text(encoding="utf-8") if research_skill_path.exists() else ""

investigator_skill_path = root / "skills" / "investigator" / "SKILL.md"
investigator_skill_text = investigator_skill_path.read_text(encoding="utf-8") if investigator_skill_path.exists() else ""

agent = create_deep_agent(
    model=f"openai:{MODEL_MODEL}",
    system_prompt=(
        "You are homelab assistant. Your goal is to work with the user and improve their homelab setup. "
        "You have access to subagents that can perform research, investigation, and other tasks to help you achieve your goal. "
        "Refer to your skills and subagents when necessary to accomplish your tasks. Always think step by step and use your subagents when you need to perform specific tasks."
    ),
    skills=[research_skill_text, investigator_skill_text],
    subagents=[investigator, research_agent]
)

agent = agent.with_config({"callbacks": [langfuse_handler]})
