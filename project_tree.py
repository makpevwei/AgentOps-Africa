import os

ROOT = "agentops"


def print_tree(folder, level=0, max_level=2):
    if level > max_level:
        return

    try:
        items = sorted(os.listdir(folder))
    except FileNotFoundError:
        print(f"Folder '{ROOT}' not found.")
        return

    items = [i for i in items if not i.startswith(".")]

    for item in items:
        path = os.path.join(folder, item)
        indent = "    " * level

        if os.path.isdir(path):
            print(f"{indent}📁 {item}/")
            print_tree(path, level + 1, max_level)
        else:
            print(f"{indent}📄 {item}")


print(f"📁 {ROOT}/")
print_tree(ROOT)
