from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)


from services import analyze_resume



router = APIRouter()



@router.post("/analyze")
async def analyze(

    file: UploadFile = File(...),

    job_description: str = Form(...)

):


    result = analyze_resume(

        file,

        job_description

    )


    return {

        "analysis": result

    }