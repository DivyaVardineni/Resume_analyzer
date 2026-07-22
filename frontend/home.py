import streamlit as st

from utils import analyze_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)


st.title("Resume Analyzer Home")



st.markdown(
"""
## Welcome to AI Resume Analyzer

Features:

✅ Resume PDF Upload

✅ AI Resume Scoring

✅ Skill Extraction

✅ Missing Skill Detection

✅ Career Suggestions

Navigate to upload your resume.
"""
)


if st.button("Next"):
    st.switch_page(
                 "pages/app.py"
             )


