# AI Study Assistant

A small command-line AI study assistant I built with Python and the OpenAI API while learning how to build LLM applications.

## What it can do

* Explain programming and CS concepts
* Generate interview questions and model answers
* Summarize text
* Create coding exercises

The interview-question feature uses **Pydantic structured outputs**, so the AI response is returned as a structured Python object instead of just plain text.

## Tech Stack

* Python
* OpenAI API
* Pydantic
* python-dotenv

## Project Structure

```text
ai-study-assistant/
├── main.py
├── ai.py
├── prompt.py
├── models.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Run Locally

1. Clone the repository. -> https://github.com/Derobm-code/AI-Study-Assistant.git
2. Create and activate a virtual environment.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

5. Run:

```bash
python main.py
```

## What I Learned

This project helped me practice:

* Working with LLM APIs
* Prompt design
* Structured outputs
* Pydantic models
* Input validation
* Basic error handling
* Organizing a Python project

## What's Next

I'm continuing to develop this project as I learn more about LLM engineering, including embeddings, semantic search, RAG, AI agents, and eventually a web-based version.

**Note:** The `.env` file is not included in the repository. Add your own OpenAI API key locally.
