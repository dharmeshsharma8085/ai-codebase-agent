from langgraph.graph import StateGraph, START, END

from graph.state import AgentState

from graph.nodes import (
    router_node,
    explorer_node,
    debugger_node,
    architecture_node,
    coding_node,
    error_node,
)

workflow = StateGraph(AgentState)


# Nodes
workflow.add_node("router", router_node)
workflow.add_node("explorer", explorer_node)
workflow.add_node("debugger", debugger_node)
workflow.add_node("architecture", architecture_node)
workflow.add_node("coding", coding_node)
workflow.add_node("error", error_node)

# START → Router
workflow.add_edge(START, "router")


def route_agent(state: AgentState):
    """Route the workflow based on router result."""

    if state.get("error"):
        return "error"

    return state["agent"]


# Router → Agent / Error
workflow.add_conditional_edges(
    "router",
    route_agent,
    {
        "explorer": "explorer",
        "debugger": "debugger",
        "architecture": "architecture",
        "coding": "coding",
    
        
    },
)


# Agent → END
workflow.add_edge("explorer", END)
workflow.add_edge("debugger", END)
workflow.add_edge("architecture", END)
workflow.add_edge("coding", END)
workflow.add_edge("error", END)


# Compile
app = workflow.compile()