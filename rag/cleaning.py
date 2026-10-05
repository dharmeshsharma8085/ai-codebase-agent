import os


IGNORED_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules"
}

IGNORED_FILES = {
    ".env"
}

ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".java",
    ".cpp",
    ".h",
    ".json",
    ".yaml",
    ".yml",
    ".md",
    ".txt"
}


def clean_repository(repo_path: str):
    cleaned_files = []

    for root, dirs, files in os.walk(repo_path):

        # Remove unwanted directories
        dirs[:] = [
            directory
            for directory in dirs
            if directory not in IGNORED_DIRS
        ]

        for file in files:

            if file in IGNORED_FILES:
                continue

            extension = os.path.splitext(file)[1].lower()

            if extension not in ALLOWED_EXTENSIONS:
                continue

            file_path = os.path.join(root, file)
            cleaned_files.append(file_path)

    return cleaned_files