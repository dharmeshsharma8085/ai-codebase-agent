from fastapi import APIRouter
from pydantic import BaseModel

from services.codebase_service import ask_codebase


router = APIRouter()


class AskRequest(BaseModel):
    repo_url: str
    question: str


@router.post("/ask")
def ask_codebase_endpoint(request: AskRequest):
    """Ask a question about a GitHub codebase."""

    response = ask_codebase(
        request.repo_url,
        request.question
    )

    return {
        "response": response
    }