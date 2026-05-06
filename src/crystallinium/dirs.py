from pathlib import Path

def find_project_root() -> Path:
    path = Path(__file__).resolve()
    proj_markers = ["pyproject.toml", ".git"]

    for parent in path.parents:
        for marker in proj_markers:
            if (parent / marker).exists():
                return parent

    raise RuntimeError("Project root not found")
