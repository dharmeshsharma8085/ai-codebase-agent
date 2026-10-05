import os

from langchain_core.documents import Document

from rag.extraction import extract_code_structure
from rag.loader import load_repository


def create_chunks(repo_url: str):
    """Create code-aware chunks from Python files."""

    documents = load_repository(repo_url)

    repo_name = (
        repo_url
        .strip()
        .rstrip("/")
        .split("/")[-1]
        .replace(".git", "")
    )

    chunks = []

    for document in documents:

        source = document.metadata.get("source", "")

        repo_marker = os.path.join(
            "data",
            "repositories",
            repo_name,
        )

        if source.startswith(repo_marker):
            relative_path = os.path.relpath(
                source,
                repo_marker,
            )
        else:
            relative_path = source

        structure = extract_code_structure(source)

        # Create chunks for functions
        for function in structure["functions"]:

            chunks.append(
                Document(
                    page_content=function["code"],
                    metadata={
                        "repository": repo_name,
                        "file": relative_path,
                        "language": "python",
                        "type": "function",
                        "name": function["name"],
                        "start_line": function["start_line"],
                        "end_line": function["end_line"],
                    },
                )
            )

        # Create chunks for classes
        for class_info in structure["classes"]:

            chunks.append(
                Document(
                    page_content=class_info["code"],
                    metadata={
                        "repository": repo_name,
                        "file": relative_path,
                        "language": "python",
                        "type": "class",
                        "name": class_info["name"],
                        "start_line": class_info["start_line"],
                        "end_line": class_info["end_line"],
                    },
                )
            )

    if not chunks:
        raise ValueError(
            "No code-aware chunks were created."
        )

    return chunks