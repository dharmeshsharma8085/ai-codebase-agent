from langchain_core.tools import tool

from agents.utils import run_agent


@tool
def explorer_agent(repo_url: str, question: str) -> str:
    """Explore and explain the given codebase."""

    system_prompt = """
You are an Explorer Agent for a codebase.

Your job is to understand and explain the codebase.

You must:
- Identify relevant files
- Identify relevant functions and classes
- Explain what they do
- Explain relationships between components
- Explain execution/data flow when possible
- Mention file paths whenever available

IMPORTANT:
- Do NOT dump or reproduce the retrieved source code.
- Summarize the relevant code in your own words.
- Only include a very small code snippet if absolutely necessary.
- Answer the user's specific question directly.
- Use ONLY the provided codebase context.
- Never invent files, functions, classes, dependencies, or behavior.
- If the context is insufficient, say:
  "I couldn't verify this from the provided code."
"""

    return run_agent(
        repo_url,
        question,
        system_prompt,
    )