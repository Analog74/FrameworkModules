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

print("README.md updated with file tree.")