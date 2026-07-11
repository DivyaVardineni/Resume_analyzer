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

result = st.session_state[
    "result"
]


st.header(
"AI Feedback"
)

st.write(result)

# analysis=result["analysis"]



# # Remove markdown code block markers
# analysis = analysis.replace("```json", "").replace("```", "").strip()

# # Convert JSON string to dict
# analysis = json.loads(analysis)

# st.subheader("Resume Score")
# st.write(analysis["score"])
# st.subheader("Skills")
# for i in analysis["skills"]:
#     st.write(
#              "✅",
#              i
#          )
# st.subheader("Missing Skills")
# for i in analysis["missing_skills"]:
#     st.write(
#              "⚠️",
#              i
#          )
# st.subheader("Experience Analysis")
# st.write(analysis["experience_analysis"])
# st.subheader("Suggestions")
# st.write(analysis["suggestions"])






