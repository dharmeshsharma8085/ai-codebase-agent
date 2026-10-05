from graph.workflow import app


def ask_codebase(repo_url: str, question: str) -> str:
    """Ask a question about a specific codebase."""

    repo_url = repo_url.strip()
    question = question.strip()

    if not repo_url:
        return "Repository URL cannot be empty."

    if not question:
        return "Question cannot be empty."

    result = app.invoke({
        "repo_url": repo_url,
        "question": question,
        "agent": "",
        "response": "",
        "error": "",
    })

    if result.get("error"):
        return result.get(
            "response",
            "I couldn't process your request."
        )

    return result["response"]