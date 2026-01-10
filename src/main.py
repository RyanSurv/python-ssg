import os
import shutil

from textnode import TextType, TextNode


def main():
    src = "static"
    dest = "public"

    if not os.path.isdir(src):
        print("src directory does not exist")
        os._exit(1)
    if not os.path.isdir(dest):
        print("dest directory does not exist")
        os._exit(1)

    empty_dir(dest)
    copy_dir(src, dest)

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