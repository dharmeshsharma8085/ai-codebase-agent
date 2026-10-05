import os

from git import Repo
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)


def load_repository(url: str):
    """Clone or update a GitHub repository and load its Python files."""

    url = url.strip()

    if not url:
        raise ValueError("Repository URL cannot be empty.")

    repo_name = (
        url.rstrip("/")
        .split("/")[-1]
        .replace(".git", "")
    )

    repo_path = os.path.join(
        "data",
        "repositories",
        repo_name,
    )

    # Clone repository if it does not already exist
    if not os.path.exists(repo_path):
        print(f"Cloning repository: {repo_name}")
        Repo.clone_from(url, repo_path)

    else:
        # Open existing local Git repository
        repo = Repo(repo_path)

        print(f"Updating repository: {repo_name}")

        # Fetch latest changes from GitHub
        repo.remotes.origin.fetch()

        # Pull latest changes into local repository
        repo.remotes.origin.pull()

    # Load Python files as plain text
    loader = DirectoryLoader(
        repo_path,
        glob="**/*.py",
        loader_cls=TextLoader,
        recursive=True,
        show_progress=True,
    )

    documents = loader.load()

    if not documents:
        raise ValueError(
            "No Python files were found in the repository."
        )

    return documents