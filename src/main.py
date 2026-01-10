import os
import shutil
import sys

from textnode import TextType, TextNode
from generate_page import generate_pages_recursive


def main():
    src = "static"
    dest = "docs"

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if not os.path.isdir(src):
        print("src directory does not exist")
        os._exit(1)
    if not os.path.isdir(dest):
        os.mkdir(dest)

    empty_dir(dest)
    copy_dir(src, dest)

    generate_pages_recursive("content", "template.html", dest, basepath)

def empty_dir(path_to_dir):
    contents = os.listdir(path_to_dir)
    for content in contents:
        path = path_to_dir + "/" + content        
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

def copy_dir(src, dest):
    contents = os.listdir(src)
    for content in contents:
        path = src + "/" + content        
        if os.path.isfile(path):
            shutil.copy(path, dest)
        elif os.path.isdir(path):
            joined_dest = os.path.join(dest, content)
            os.mkdir(joined_dest)
            copy_dir(path, joined_dest)



main()