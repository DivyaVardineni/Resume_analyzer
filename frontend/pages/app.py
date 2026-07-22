import streamlit as st
from utils import analyze_resume


st.title(
    " 🤖 AI Resume Analyzer"
)



uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Enter the job description here..."
)



if st.button("Analyze Resume"):


    if uploaded_file is None:

        st.warning(
            "Please upload a resume PDF."
        )


    elif not job_description.strip():

        st.warning(
            "Please enter a job description."
        )


    else:

        with st.spinner("Analyzing resume..."):


            result = analyze_resume(

                uploaded_file,

                job_description

            )


            st.session_state["result"] = result


            st.success(
                "Analysis completed"
            )


            st.switch_page(
                "pages/results.py"
            )




