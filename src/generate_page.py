import os
from pathlib import Path

from markdown import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        print("From path does not exist")
        os._exit(1)
    if not os.path.exists(template_path):
        print("Template path does not exist")
        os._exit(1)

    open_f = open(from_path, 'r', encoding="utf-8")
    template_f = open(template_path, 'r', encoding="utf-8")

    open_contents = open_f.read()
    template_contents = template_f.read()

    content = markdown_to_html_node(open_contents).to_html()
    title = extract_title(open_contents)
    print(title)

    replaced = template_contents.replace("{{ Title }}", title)
    replaced = replaced.replace("{{ Content }}", content)

    dest_f = open(dest_path, 'w', encoding="utf-8")
    dest_f.write(replaced)

    open_f.close()
    template_f.close()
    dest_f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        path = dir_path_content + "/" + content
        if os.path.isfile(path) and Path(path).suffix == ".md":
            generate_page(path, "template.html", dest_dir_path + "/" + Path(content).stem + ".html")
        elif os.path.isdir(path):
            joined_dest = os.path.join(dest_dir_path, content)
            os.mkdir(joined_dest)
            generate_pages_recursive(path, "template.html", joined_dest)
