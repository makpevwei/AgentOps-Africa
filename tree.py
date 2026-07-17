import os
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."

def show(folder, level=0):
    if level > 4:
        return

    try:
        items = sorted(os.listdir(folder))
    except FileNotFoundError:
        print(f"❌ Folder '{folder}' not found.")
        return

    for item in items:
        if item.startswith("."):
            continue

        path = os.path.join(folder, item)
        indent = "    " * level

        if os.path.isdir(path):
            print(f"{indent}📁 {item}/")
            show(path, level + 1)
        else:
            print(f"{indent}📄 {item}")

print(f"\n📁 {ROOT}/")
show(ROOT)