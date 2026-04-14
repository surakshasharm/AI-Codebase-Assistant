from git import Repo
from pathlib import Path

# Base directory where repos will be stored
BASE_DIR = Path("data/repos")

# Only include useful code files
SUPPORTED_EXTENSIONS = {
    ".py"
}

# Ignore unnecessary directories
IGNORE_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    "venv",
    ".venv",
    "build",
    "dist"
}


def clone_repo(repo_url: str):
    BASE_DIR.mkdir(parents=True, exist_ok=True)

    repo_name = repo_url.split("/")[-1]
    clone_path = BASE_DIR / repo_name

    if clone_path.exists():
        return str(clone_path)

    Repo.clone_from(repo_url, clone_path)
    return str(clone_path)


def get_source_files(repo_path: str):
    repo_path = Path(repo_path)
    files = []

    for file in repo_path.rglob("*"):
        if file.is_file() and file.suffix in SUPPORTED_EXTENSIONS:

            # Ignore unwanted folders
            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            # 🔥 Ignore test files
            if "test" in file.name.lower():
                continue

            files.append(str(file))

    return files