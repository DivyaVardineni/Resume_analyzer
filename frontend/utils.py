import requests


BACKEND_URL="http://localhost:8000/api"



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