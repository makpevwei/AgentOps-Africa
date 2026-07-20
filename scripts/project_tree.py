from pathlib import Path

MAX_DEPTH = 4

IGNORE = {
    ".git",
    ".next",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    ".pytest_cache",
    ".ruff_cache",
    "dist",
    "build",
    ".DS_Store",
}


def walk(path: Path, prefix="", depth=0):
    if depth > MAX_DEPTH:
        return

    items = sorted(
        [p for p in path.iterdir() if p.name not in IGNORE],
        key=lambda p: (p.is_file(), p.name.lower()),
    )

    for i, item in enumerate(items):
        last = i == len(items) - 1
        branch = "└── " if last else "├── "

        icon = "📁" if item.is_dir() else "📄"

        print(prefix + branch + f"{icon} {item.name}")

        if item.is_dir():
            extension = "    " if last else "│   "
            walk(item, prefix + extension, depth + 1)


if __name__ == "__main__":
    root = Path(".")
    print(f"\nProject: {root.resolve()}\n")
    walk(root)
