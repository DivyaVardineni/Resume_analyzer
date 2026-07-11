import requests
import streamlit as st

BACKEND_URL=st.secrets["backend_url"]



def analyze_resume(file, job_description):


    response=requests.post(

        f"{BACKEND_URL}/analyze",

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


    return response.json()