from agents.explorer_agent import explorer_agent
from agents.debugger_agent import debugger_agent
from agents.architecture import architecture_agent
from agents.coding import coding_agent

from rag.llm import llm
from graph.state import AgentState


VALID_AGENTS = {
    "explorer",
    "debugger",
    "architecture",
    "coding",
}


def router_node(state: AgentState):
    """Decide which specialized agent should handle the question."""

    question = state["question"].strip()

    if not question:
        return {
            "agent": "",
            "error": "User question cannot be empty.",
        }

    prompt = f"""
You are the routing system for an AI Codebase Assistant.

Choose exactly ONE agent.

Available agents:

explorer:
- Understand existing code
- Find files, functions, and classes
- Explain existing behavior

debugger:
- Analyze bugs
- Analyze exceptions and errors
- Find root causes

architecture:
- Explain system architecture
- Explain components and relationships
- Explain dependencies and data flow

coding:
- Implement features
- Modify existing code
- Refactor code
- Generate code changes

Return ONLY one of:

explorer
debugger
architecture
coding

Do not return explanations.
Do not return markdown.
Do not return any other text.

USER QUESTION:
{question}
"""

    try:
        response = llm.invoke(prompt)

        agent = response.content.strip().lower()

        if agent not in VALID_AGENTS:
            return {
                "agent": "",
                "error": f"Router returned an invalid agent: {agent}",
            }

        return {
            "agent": agent,
            "error": "",
        }

    except Exception as exc:
        return {
            "agent": "",
            "error": f"Router failed: {str(exc)}",
        }


def explorer_node(state: AgentState):
    """Run the Explorer Agent."""

    try:
        response = explorer_agent.invoke({
            "repo_url": state["repo_url"],
            "question": state["question"],
        })

        return {
            "response": response,
            "error": "",
        }

    except Exception as exc:
        return {
            "response": "",
            "error": f"Explorer Agent failed: {str(exc)}",
        }


def debugger_node(state: AgentState):
    """Run the Debugger Agent."""

    try:
        response = debugger_agent.invoke({
            "repo_url": state["repo_url"],
            "question": state["question"],
        })

        return {
            "response": response,
            "error": "",
        }

    except Exception as exc:
        return {
            "response": "",
            "error": f"Debugger Agent failed: {str(exc)}",
        }


def architecture_node(state: AgentState):
    """Run the Architecture Agent."""

    try:
        response = architecture_agent.invoke({
            "repo_url": state["repo_url"],
            "question": state["question"],
        })

        return {
            "response": response,
            "error": "",
        }

    except Exception as exc:
        return {
            "response": "",
            "error": f"Architecture Agent failed: {str(exc)}",
        }


def coding_node(state: AgentState):
    """Run the Coding Agent."""

    try:
        response = coding_agent.invoke({
            "repo_url": state["repo_url"],
            "question": state["question"],
        })

        return {
            "response": response,
            "error": "",
        }

    except Exception as exc:
        return {
            "response": "",
            "error": f"Coding Agent failed: {str(exc)}",
        }


def error_node(state: AgentState):
    """Handle workflow errors."""

    error = state.get("error", "Unknown workflow error.")

    return {
        "response": (
            "I couldn't process your request because "
            "an internal workflow error occurred.\n\n"
            f"Details: {error}"
        ),
        "error": error,
    }