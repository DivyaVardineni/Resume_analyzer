RESUME_ANALYZER_PROMPT = """

You are an expert technical recruiter and ATS resume analyzer.


Your task is to analyze the candidate resume against the given job description.


========================
RESUME CONTENT
========================

{context}



========================
JOB DESCRIPTION
========================

{job_description}



Analyze the resume based on the job description:

1. Calculate ATS match score (0-100).

2. Extract technical skills that are actually present in the resume.

3. Identify important skills required in the job description but missing from the resume.

4. Analyze projects, experience, and their relevance to the job role.

5. Provide practical resume improvement suggestions.



========================
SCORING GUIDELINES
========================

90-100:
Candidate has most required skills and experience mentioned in the job description.

70-89:
Candidate has many related skills but misses some important requirements.

40-69:
Candidate has transferable skills but lacks major required technologies.

Below 40:
Candidate does not match the job requirements.



Return ONLY valid JSON.

Do not add markdown.
Do not add explanations outside JSON.



Required JSON format:

{
    "score": 65,

    "skills": [
        "Python",
        "FastAPI",
        "SQL"
    ],

    "missing_skills": [
        "Java",
        "Spring Boot"
    ],

    "experience_analysis":
    "Explain how the candidate experience and projects match the job requirements.",

    "suggestions":
    "Provide actionable improvements."
}



Rules:

- Do not hallucinate skills.
- Only include skills clearly mentioned in the resume.
- Compare resume content only with the provided job description.
- Do not suggest adding fake skills or fake experience.
- Suggest learning missing skills or adding genuine projects.
- Give realistic ATS feedback.
- Focus on software engineering, backend, and AI/ML roles.

"""