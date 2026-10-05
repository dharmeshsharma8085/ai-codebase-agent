import json
import os

from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from rag.chunking import create_chunks
from rag.loader import load_repository

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


def get_repo_name(repo_url: str) -> str:
    """Extract repository name from GitHub URL."""
    return (
        repo_url
        .strip()
        .rstrip("/")
        .split("/")[-1]
        .replace(".git", "")
    )


def get_repo_commit(repo_url: str) -> str:
    """Update the local repository and return its latest commit SHA."""

    load_repository(repo_url)

    repo_name = get_repo_name(repo_url)

    repo_path = os.path.join(
        "data",
        "repositories",
        repo_name,
    )

    from git import Repo

    repo = Repo(repo_path)

    return repo.head.commit.hexsha


def get_metadata_path(persist_directory: str) -> str:
    """Return the path of the repository metadata file."""

    return os.path.join(
        persist_directory,
        "metadata.json",
    )


def load_saved_commit(persist_directory: str):
    """Load the previously indexed commit SHA."""

    metadata_path = get_metadata_path(
        persist_directory
    )

    if not os.path.exists(metadata_path):
        return None

    with open(
        metadata_path,
        "r",
        encoding="utf-8",
    ) as file:
        metadata = json.load(file)

    return metadata.get("commit_sha")


def save_commit(
    persist_directory: str,
    commit_sha: str,
):
    """Save the commit SHA used for the current index."""

    os.makedirs(
        persist_directory,
        exist_ok=True,
    )

    metadata_path = get_metadata_path(
        persist_directory
    )

    with open(
        metadata_path,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            {
                "commit_sha": commit_sha
            },
            file,
            indent=4,
        )


def create_vectorstore(repo_url: str):
    """Create or load a repository-specific Chroma vector store."""

    repo_name = get_repo_name(repo_url)

    persist_directory = os.path.join(
        "chroma-db",
        repo_name,
    )

    current_commit = get_repo_commit(repo_url)

    saved_commit = load_saved_commit(
        persist_directory
    )

    # Existing index is up-to-date
    if (
        os.path.exists(persist_directory)
        and saved_commit == current_commit
    ):
        print(
            f"Loading existing vectorstore: {repo_name}"
        )

        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model,
        )

    # Repository is new or has changed
    print(
        f"Indexing repository: {repo_name}"
    )

    chunks = create_chunks(repo_url)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )

    save_commit(
        persist_directory,
        current_commit,
    )

    return vectorstore