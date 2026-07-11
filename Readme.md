# AI Resume Analyzer

An AI-powered Resume Analyzer built using **FastAPI**, **Streamlit**, **PyPDF2**, **LangChain**, **Hugging Face Embeddings**, **Pinecone**, and **Groq LLM**. It analyzes PDF resumes and provides insights such as resume score, skills, missing skills, experience analysis, and improvement suggestions.

## Features

- Upload PDF resumes
- Extract text using PyPDF2
- Generate embeddings using Hugging Face (`all-MiniLM-L6-v2`)
- Store and retrieve vectors using Pinecone
- Analyze resumes using Groq LLM
- Display:
  - Resume Score
  - Skills
  - Missing Skills
  - Experience Analysis
  - Suggestions

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **LLM:** Groq (Llama 3.1)
- **Embeddings:** Hugging Face (`all-MiniLM-L6-v2`)
- **Vector Database:** Pinecone
- **PDF Processing:** PyPDF2

## Project Structure

```
resume-analyzer/
│── frontend/
│── backend/
│── uploads/
│── .env
│── requirements.txt
│── README.md
```

## Workflow

```
Resume PDF
    ↓
PyPDF2
    ↓
Text Chunking
    ↓
Hugging Face Embeddings
    ↓
Pinecone
    ↓
Groq LLM
    ↓
Resume Analysis
```


