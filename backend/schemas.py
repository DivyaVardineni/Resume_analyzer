from pydantic import BaseModel

from typing import List



class AnalyzeResponse(BaseModel):

    score: int

    skills: List[str]

    missing_skills: List[str]

    experience_analysis: str

    suggestions: str