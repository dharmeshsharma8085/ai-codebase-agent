from rag.retriever import create_retriever
from rag.llm import llm

def get_codebase_context(repo_url: str, question: str) -> str:
    """Retrieve relevant context from the given repository."""

    retriever = create_retriever(repo_url)

    relevant_chunks = retriever.invoke(question)

    context = "\n\n".join(
        f"REPOSITORY: {chunk.metadata.get('repository', 'Unknown')}\n"
        f"FILE: {chunk.metadata.get('file', chunk.metadata.get('source', 'Unknown'))}\n"
        f"LANGUAGE: {chunk.metadata.get('language', 'Unknown')}\n"
        f"CODE:\n{chunk.page_content}"
        for chunk in relevant_chunks
    )

    return context


def run_agent(
    repo_url: str,
    question: str,
    system_prompt: str,
) -> str:
    """Retrieve repository context and run an agent."""

    context = get_codebase_context(
        repo_url,
        question,
    )

    prompt = f"""
{system_prompt}

CODEBASE CONTEXT:
{context}

USER QUESTION:
{question}
"""

    response = llm.invoke(prompt)

    return response.content