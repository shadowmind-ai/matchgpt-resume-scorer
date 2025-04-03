from fastapi import FastAPI

app = FastAPI(
    title="MatchGPT API",
    description="Backend service for scoring resume and job description matches.",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
