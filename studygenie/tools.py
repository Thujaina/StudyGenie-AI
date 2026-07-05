from google.adk.tools import FunctionTool

from .pdf_tools import extract_pdf_text


def generate_quiz(topic: str) -> str:
    return f"""
Quiz on {topic}

1. What is {topic}?
2. Why is {topic} important?
3. Give one real-world application of {topic}.
4. State one advantage of {topic}.
5. State one limitation of {topic}.
"""


def generate_flashcards(topic: str) -> str:
    return f"""
Flashcards on {topic}

Front: What is {topic}?
Back: A simple explanation of {topic}.

Front: Why is {topic} important?
Back: It helps learners understand key ideas and applications.

Front: Give one example of {topic}?
Back: Example depends on the subject context.
"""


def generate_study_plan(topic: str) -> str:
    return f"""
Study Plan for {topic}

Session 1: Understand the basics of {topic}
Session 2: Learn key definitions and concepts
Session 3: Study examples and applications
Session 4: Practice questions
Session 5: Final revision and self-test

Revision Tip:
After each session, write a short summary in your own words.
"""


quiz_tool = FunctionTool(generate_quiz)
flashcard_tool = FunctionTool(generate_flashcards)
study_plan_tool = FunctionTool(generate_study_plan)
pdf_tool = FunctionTool(extract_pdf_text)