import os
import re

branch = "main"
root_dir = "."
repo_url = "https://github.com/Analog74/FrameworkModules/blob"
readme_file = "README.md"
start_marker = "<!-- FILETREE-START -->"
end_marker = "<!-- FILETREE-END -->"

output_lines = []

def add_entry(path, depth):
    filename = os.path.basename(path)
    url_path = os.path.relpath(path, root_dir).replace("\\", "/")
    if os.path.isdir(path):
        md_link = f"**[{filename}]({repo_url}/{branch}/{url_path})**"
    else:
        md_link = f"[{filename}]({repo_url}/{branch}/{url_path})"
    output_lines.append(f"{'  ' * depth}- {md_link}")

def walk(dirpath, depth=0):
    entries = sorted(os.listdir(dirpath))
    for entry in entries:
        if entry.startswith('.') or entry in [readme_file, '.git']:
            continue
        full_path = os.path.join(dirpath, entry)
        add_entry(full_path, depth)
        if os.path.isdir(full_path):
            walk(full_path, depth + 1)

walk(root_dir)
filetree_md = "\n".join(output_lines)

# Read the README file
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        readme = f.read()
else:
    readme = "# FrameworkModules\n"

# Prepare filetree section
filetree_section = f"{start_marker}\n\n### Repository File Tree\n\n" + filetree_md + f"\n\n{end_marker}"

# Replace or append filetree section
if start_marker in readme and end_marker in readme:
    new_readme = re.sub(f"{start_marker}.*?{end_marker}", filetree_section, readme, flags=re.DOTALL)
else:
    new_readme = readme.rstrip() + "\n\n" + filetree_section

with open(readme_file, "w", encoding="utf-8") as f:
    f.write(new_readme)


# --- Directory and File Index Generation ---
from collections import defaultdict

def get_dir_purpose(path):
    # Customize as needed for your project
    mapping = {
        "src/ReplicatedStorage": "Shared modules and data accessible by both client and server",
        "src/ServerScriptService": "Server-side scripts and logic",
        "src/ReplicatedStorage/Modules": "Core gameplay and utility modules",
        "src/ReplicatedStorage/Packages": "Package modules and dependencies",
        "src/ReplicatedStorage/ThirdParty": "Third-party libraries",
        "docs": "Project documentation and indexes",
    }
    return mapping.get(path, "-")

def get_key_subfolders(path):
    try:
        subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and not f.startswith('.')]
        return ", ".join(f"{f}/" for f in sorted(subfolders)) if subfolders else "-"
    except Exception:
        return "-"

# Gather directory info
dir_rows = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    rel_dir = os.path.relpath(dirpath, root_dir).replace("./", "").replace(".\\", "")
    if rel_dir == "." or rel_dir.startswith(".git") or rel_dir.startswith("__pycache__"):
        continue
    if rel_dir == "":
        continue
    purpose = get_dir_purpose(rel_dir)
    key_subfolders = get_key_subfolders(dirpath)
    dir_rows.append((rel_dir, purpose, key_subfolders))

# Write DIRECTORY_INDEX.md
dir_index_md = [
    "# Directory Index\n",
    "This document provides an overview of all major directories in the project, their purpose, and key subfolders.\n",
    "| Directory | Purpose | Key Subfolders |",
    "|-----------|---------|---------------|",
]
for row in dir_rows:
    dir_index_md.append(f"| {row[0]} | {row[1]} | {row[2]} |")
with open("docs/DIRECTORY_INDEX.md", "w", encoding="utf-8") as f:
    f.write("\n".join(dir_index_md) + "\n")

# Write DIRECTORY_INDEX.json
import json
dir_index_json = [
    {"path": row[0], "purpose": row[1], "keySubfolders": [s.strip() for s in row[2].split(",") if s.strip() and s.strip() != "-"]}
    for row in dir_rows
]
with open("docs/DIRECTORY_INDEX.json", "w", encoding="utf-8") as f:
    json.dump({"directories": dir_index_json}, f, indent=2)

# Gather file info
file_rows = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    rel_dir = os.path.relpath(dirpath, root_dir).replace("./", "").replace(".\\", "")
    if rel_dir.startswith(".git") or rel_dir.startswith("__pycache__"):
        continue
    for filename in filenames:
        if filename.startswith('.') or filename in [readme_file, 'FILETREE.md']:
            continue
        rel_file = os.path.join(rel_dir, filename) if rel_dir else filename
        # Simple tag/description logic
        if rel_file.endswith('.luau'):
            tag = "Luau Module"
        elif rel_file.endswith('.md'):
            tag = "Markdown Doc"
        elif rel_file.endswith('.json'):
            tag = "Config/Data"
        elif rel_file.endswith('.py'):
            tag = "Script"
        else:
            tag = "-"
        file_rows.append((filename, rel_file, tag))

# Write FILE_INDEX.md
file_index_md = [
    "# File Index\n",
    "This document lists all major files in the project, their location, and a brief description or tag.\n",
    "| File | Location | Description/Tag |",
    "|------|----------|----------------|",
]
for row in file_rows:
    file_index_md.append(f"| {row[0]} | {row[1]} | {row[2]} |")
with open("docs/FILE_INDEX.md", "w", encoding="utf-8") as f:
    f.write("\n".join(file_index_md) + "\n")

# Write FILE_INDEX.json
file_index_json = [
    {"file": row[0], "location": row[1], "description": row[2]} for row in file_rows
]
with open("docs/FILE_INDEX.json", "w", encoding="utf-8") as f:
    json.dump({"files": file_index_json}, f, indent=2)

print("README.md, DIRECTORY_INDEX.md, FILE_INDEX.md, and JSON indexes updated.")