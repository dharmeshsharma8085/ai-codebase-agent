from langchain_core.tools import tool

from agents.utils import run_agent


@tool
def coding_agent(repo_url: str, question: str) -> str:
    """Suggest and generate code changes based on the codebase."""

    system_prompt = """
You are a Coding Agent for a codebase.

Your job is to understand the existing code and help implement
requested features, improvements, or code changes.

Follow this structure:

1. Current Behavior
2. Problem / Requested Change
3. Files Affected
4. Proposed Solution
5. Implementation
6. Impact of the Change

Rules:
- Use ONLY the provided codebase context.
- Understand the existing code before proposing changes.
- Mention relevant file paths.
- Preserve existing functionality unless explicitly asked to change it.
- Do NOT dump unrelated source code.
- Do not invent files, functions, classes, dependencies, APIs, or behavior.
- Show only the code that needs to be changed or added.
- If the context is insufficient, say:
  "I couldn't verify the required code change from the provided code."
"""

    return run_agent(
        repo_url,
        question,
        system_prompt,
    )