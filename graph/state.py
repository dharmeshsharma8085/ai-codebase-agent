from typing import TypedDict


class AgentState(TypedDict):
    repo_url: str
    question: str
    agent: str
    response: str
    error: str