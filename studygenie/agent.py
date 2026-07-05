from pathlib import Path

from google.adk.agents import Agent

from .config import MODEL_NAME, APP_DESCRIPTION
from .tools import quiz_tool, flashcard_tool, study_plan_tool, pdf_tool

SYSTEM_PROMPT = Path(__file__).parent.joinpath(
    "prompts", "system_prompt.txt"
).read_text()

root_agent = Agent(
    name="studygenie",
    model=MODEL_NAME,
    description=APP_DESCRIPTION,
    instruction=SYSTEM_PROMPT,
    tools=[quiz_tool, flashcard_tool, study_plan_tool, pdf_tool],
)