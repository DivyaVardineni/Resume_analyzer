import streamlit as st
import json



st.title(
    "📊 Resume Analysis Result"
)



if "result" not in st.session_state:


    st.warning(
        "Please analyze a resume first"
    )

    st.stop()



result = st.session_state["result"]



if result is None:


    st.error(
        "Unable to analyze resume. Please try again."
    )

    st.stop()



st.header(
    "AI Feedback"
)



analysis = result.get(
    "analysis"
)



if not analysis:


    st.error(
        "No analysis result received from backend."
    )

    st.stop()



# Remove markdown formatting if returned by LLM

analysis = analysis.replace(
    "```json",
    ""
)

analysis = analysis.replace(
    "```",
    ""
).strip()



try:

    analysis = json.loads(
        analysis
    )


except json.JSONDecodeError:


    st.error(
        "AI response format error."
    )

    st.write(
        analysis
    )

    st.stop()



st.subheader(
    "Resume Score"
)

st.write(
    analysis.get("score", "N/A")
)



st.subheader(
    "Skills"
)

for skill in analysis.get("skills", []):

    st.write(
        "✅",
        skill
    )



st.subheader(
    "Missing Skills"
)

for skill in analysis.get("missing_skills", []):

    st.write(
        "⚠️",
        skill
    )



st.subheader(
    "Experience Analysis"
)

st.write(
    analysis.get(
        "experience_analysis",
        "N/A"
    )
)



st.subheader(
    "Suggestions"
)

st.write(
    analysis.get(
        "suggestions",
        "N/A"
    )
)