import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path, basepath):
    file = open(from_path)
    contents = file.read()
    file.close()

    file = open(template_path)
    template = file.read()
    file.close()

    content = markdown_to_html_node(contents)
    html = content.to_html()

    title = extract_title(contents)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    file = open(dest_path, "w")
    file.write(template)
    file.close()

def generate_pages_recursive(dir_path, template_path, dest_dir, basepath):
    for each_entry in os.listdir(dir_path):
        from_path = os.path.join(dir_path, each_entry)
        dest_path = os.path.join(dest_dir, each_entry)

        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
