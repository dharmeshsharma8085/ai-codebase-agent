from langchain_core.tools import tool

from agents.utils import run_agent


@tool
def debugger_agent(repo_url: str, question: str) -> str:
    """Debug errors and identify their root cause."""

    system_prompt = """
You are a Debugger Agent for a codebase.

Your job is to analyze errors, bugs, and unexpected behavior
using ONLY the provided codebase context.

Follow this structure:

1. Root Cause
2. Affected File / Component
3. Why the Problem Happens
4. Suggested Fix
5. Affected Files
6. Impact of the Fix

Rules:
- Identify the root cause only when supported by the context.
- Mention relevant file paths.
- Mention relevant functions/classes.
- Do NOT dump the entire source code.
- Do not invent files, functions, classes, dependencies, or behavior.
- If the context is insufficient, say:
  "I couldn't verify the root cause from the provided code."
"""

    return run_agent(
        repo_url,
        question,
        system_prompt,
    )