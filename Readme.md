# AI Resume Analyzer

An AI-powered Resume Analyzer built using **FastAPI**, **Streamlit**, **PyPDF2**, **LangChain**, and **Groq LLM**. It analyzes PDF resumes by comparing them with a given job description and provides ATS-based insights such as resume score, skills, missing skills, experience analysis, and improvement suggestions.

## Features

- Upload PDF resumes
- Extract resume text using PyPDF2
- Split resume content into meaningful chunks using LangChain text splitters
- Compare resume with job description
- Analyze resumes using Groq LLM (Llama 3.1)
- Generate ATS-based feedback:
  - Resume Score
  - Available Skills
  - Missing Skills
  - Experience Analysis
  - Resume Improvement Suggestions


## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **LLM:** Groq (Llama 3.1)
- **PDF Processing:** PyPDF2
- **Text Processing:** LangChain Recursive Character Text Splitter


## Project Structure

```
resume-analyzer/
│
├── frontend/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── services.py
│   ├── routes/
│   │   └── analyze.py
│   └── prompt/
│       └── analyze_prompt.py
│
├── uploads/
│
├── .env
├── requirements.txt
└── README.md
```


## Workflow

```
Resume PDF
     ↓
PyPDF2
     ↓
Extract Resume Text
     ↓
Text Chunking
     ↓
Resume + Job Description
     ↓
Groq LLM (Llama 3.1)
     ↓
ATS Resume Analysis
     ↓
JSON Response
```


## API Endpoint

### Analyze Resume

```
POST /api/analyze
```

### Request

- Resume PDF file
- Job Description


### Response

Example:

```json
{
    "score": 85,
    "skills": [
        "Python",
        "FastAPI",
        "SQL"
    ],
    "missing_skills": [
        "Docker",
        "AWS"
    ],
    "experience_analysis": "Candidate projects align with backend development requirements.",
    "suggestions": "Add cloud deployment experience and more backend projects."
}
```


## Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```


## Future Improvements

- Add user authentication
- Add resume history tracking
- Add multiple resume comparison
- Add ATS keyword matching
- Add deployment using Docker and cloud platforms