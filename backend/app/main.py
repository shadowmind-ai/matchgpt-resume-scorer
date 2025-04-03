from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="MatchGPT API",
    description="Backend service for scoring resume and job description matches.",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

class ScoreRequest(BaseModel):
    resume: str = Field(..., min_length=10, description="Candidate resume text")
    job_description: str = Field(..., min_length=10, description="Job description text")

class ScoreResponse(BaseModel):
    match_score: float

@app.post("/score", response_model=ScoreResponse)
def score_resume(req: ScoreRequest):
    if not req.resume.strip() or not req.job_description.strip():
        raise HTTPException(status_code=400, detail="Inputs must not be empty.")

    # Dummy scoring logic — to be replaced with real AI
    score = 0.75  # Static for now
    return {"match_score": round(score, 2)}
