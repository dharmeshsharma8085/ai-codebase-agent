from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="AI Codebase Agent",
    description="AI-powered codebase analysis and assistance system",
    version="1.0.0",
)


app.include_router(router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "AI Codebase Agent API is running"
    }