from rag.vectorstore import create_vectorstore


def create_retriever(repo_url: str):
    """Create a retriever for the given repository."""

    vectorstore = create_vectorstore(repo_url)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    return retriever