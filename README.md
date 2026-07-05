# 📚 StudyGenie – Adaptive AI Study Assistant

StudyGenie is an AI-powered study assistant built for the **Kaggle AI Agents: Intensive Vibe Coding Capstone Project** using Google's Agent Development Kit (ADK), Gemini, and Streamlit.

It helps students learn more effectively by explaining concepts, generating quizzes, creating flashcards, preparing study plans, and analyzing study materials.

---

## Features

- Explain difficult concepts in simple language
- Generate quizzes
- Create flashcards
- Build personalized study plans
- Extract text from PDF study materials
- Analyze uploaded images
- Session-based conversation memory
- Secure file validation
- Prompt validation against unsafe instructions
- Streamlit web interface

---

## Technologies Used

- Google ADK
- Gemini API
- Streamlit
- Python
- PyMuPDF
- Pillow
- python-dotenv

---

## Project Structure

```
StudyGenie/
│
├── studygenie/
│   ├── agent.py
│   ├── tools.py
│   ├── pdf_tools.py
│   ├── security.py
│   ├── config.py
│   ├── prompts/
│   │    └── system_prompt.txt
│   └── .env (local only)
│
├── notebook/
├── assets/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Security

The project follows secure development practices:

- API keys are stored locally in `.env`
- `.env` is excluded using `.gitignore`
- Uploaded files are validated
- Prompt injection is partially mitigated through input validation

No API keys or secrets are included in the repository.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd StudyGenie
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file:

```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash-lite
```

---

## Running the ADK Agent

```bash
adk web
```

or

```bash
adk run studygenie
```

---

## Running the Frontend

```bash
streamlit run app.py
```

---

## AI Agent Concepts Demonstrated

This project demonstrates the concepts covered in the Kaggle AI Agents Intensive course:

- Google Agent Development Kit (ADK)
- Agent Skills / Tools
- Prompt Engineering
- Secure Agent Development
- Deployable AI Application
- Gemini Integration
- Session Memory

---

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- Vector database integration
- OCR for handwritten notes
- Multi-agent collaboration
- Cloud deployment

---

## License

This project was developed for educational purposes as part of the Kaggle AI Agents Intensive Vibe Coding Capstone Project.