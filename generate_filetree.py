import os

branch = "main"
root_dir = "."
repo_url = "https://github.com/Analog74/FrameworkModules/blob"
output_file = "FILETREE.md"

output_lines = []

def add_entry(path, depth):
    filename = os.path.basename(path)
    url_path = path.replace("\\", "/").lstrip("./")
    md_link = f"[{filename}]({repo_url}/{branch}/{url_path})" if os.path.isfile(path) else f"**[{filename}]({repo_url}/{branch}/{url_path})**"
    output_lines.append(f"{'  ' * depth}- {md_link}")

def walk(dirpath, depth=0):
    entries = sorted(os.listdir(dirpath))
    for entry in entries:
        if entry.startswith('.') or entry == output_file or entry == '.git':
            continue
        full_path = os.path.join(dirpath, entry)
        add_entry(full_path, depth)
        if os.path.isdir(full_path):
            walk(full_path, depth + 1)

walk(root_dir)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# Repository File Tree\n\n")
    for line in output_lines:
        f.write(line + "\n")

print(f"File tree written to {output_file}")