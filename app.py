
import os
import tempfile

import time
from google.genai import errors

import fitz
import streamlit as st
from google import genai
from PIL import Image
from dotenv import load_dotenv
load_dotenv("studygenie/.env")

APP_TITLE = "📚 StudyGenie"
APP_SUBTITLE = "Adaptive AI Study Coach using Gemini + ADK concepts"

SYSTEM_PROMPT = """
You are StudyGenie, an adaptive AI study coach.

Help students:
- understand study material
- summarize PDFs and notes
- explain concepts simply
- generate quizzes
- create flashcards
- create study plans

Never invent facts. If content is missing, say so clearly.
"""

ALLOWED_TYPES = ["pdf", "png", "jpg", "jpeg", "txt"]
MAX_FILE_SIZE_MB = 10


def validate_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return True

    size_mb = uploaded_file.size / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        st.error("File too large. Maximum allowed size is 10 MB.")
        return False

    ext = uploaded_file.name.split(".")[-1].lower()
    if ext not in ALLOWED_TYPES:
        st.error("Unsupported file type.")
        return False

    return True


def extract_pdf_text(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    doc = fitz.open(temp_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text


def extract_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8", errors="ignore")

def ask_gemini(client, prompt, image=None, max_retries=3):
    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")

    for attempt in range(max_retries):
        try:
            if image is not None:
                response = client.models.generate_content(
                    model=model_name,
                    contents=[prompt, image],
                )
            else:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )

            return response.text

        except errors.ServerError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return (
                    "Gemini is temporarily overloaded. "
                    "Please wait a few seconds and click Ask StudyGenie again."
                )

st.set_page_config(page_title="StudyGenie", page_icon="📚")

st.title(APP_TITLE)
st.write(APP_SUBTITLE)

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY is missing. Add it as an environment variable or Streamlit secret.")
    st.stop()

client = genai.Client(api_key=api_key)

if "memory" not in st.session_state:
    st.session_state.memory = []

uploaded_file = st.file_uploader(
    "Upload study material",
    type=ALLOWED_TYPES,
)

study_context = ""

if uploaded_file:
    if validate_uploaded_file(uploaded_file):
        file_type = uploaded_file.name.split(".")[-1].lower()

        if file_type == "pdf":
            study_context = extract_pdf_text(uploaded_file)
            st.success("PDF uploaded and processed.")

        elif file_type == "txt":
            study_context = extract_txt(uploaded_file)
            st.success("Text file uploaded and processed.")

        elif file_type in ["png", "jpg", "jpeg"]:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded image", use_container_width=True)
            study_context = "Image uploaded. Use vision model for explanation."

        else:
            image = None

task = st.selectbox(
    "Choose a task",
    [
        "Ask a question",
        "Summarize",
        "Explain simply",
        "Create quiz",
        "Create flashcards",
        "Create study plan",
    ],
)

user_question = st.text_area("Enter your question or instruction")

if st.button("Ask StudyGenie"):
    if uploaded_file and uploaded_file.name.split(".")[-1].lower() in ["png", "jpg", "jpeg"]:
        image = Image.open(uploaded_file)
        prompt = f"""
{SYSTEM_PROMPT}

Task: {task}
User instruction: {user_question}
"""
        answer = ask_gemini(client, prompt, image=image)

    else:
        prompt = f"""
{SYSTEM_PROMPT}

Previous conversation:
{st.session_state.memory[-5:]}

Study material:
{study_context}

Task:
{task}

User instruction:
{user_question}
"""
        answer = ask_gemini(client, prompt)

    st.session_state.memory.append(
        {"user": user_question, "assistant": answer}
    )

    st.subheader("StudyGenie Response")
    st.write(answer)

with st.expander("Project Concepts Demonstrated"):
    st.write("""
- ADK agent architecture
- Agent tools / skills
- Prompt engineering
- File validation
- Secure API key handling
- Session memory
- Deployable frontend
""")