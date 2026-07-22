import requests
import streamlit as st


BACKEND_URL = st.secrets["backend_url"]



def analyze_resume(file, job_description):


    response = requests.post(

        f"{BACKEND_URL}/api/analyze",

        files={

            "file":
            (
                file.name,
                file,
                "application/pdf"
            )

        },

        data={

            "job_description":
            job_description

        }

    )


    if response.status_code != 200:

        st.error(
            f"Backend Error: {response.text}"
        )

        return None



    return response.json()