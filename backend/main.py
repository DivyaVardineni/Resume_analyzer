from fastapi import FastAPI

from routes.analyze import router


app = FastAPI(
    title="Resume Analyzer AI"
)


app.include_router(
    router,
    prefix="/api"
)



@app.get("/")
def home():

    return {
        "message":
        "Resume Analyzer API Running"
    }