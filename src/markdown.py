from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    # Am I fuckin functional now or what???!
    return list(filter(lambda b: len(b) != 0, map(lambda b: b.strip(), markdown.split("\n\n"))))


def block_to_block_type(block):
    max_heading = "######"

    if not "\n" in block: # Single Line
        # HEADING
        parts = block.split(" ")
        if parts[0] in max_heading:
            return BlockType.HEADING
    else: # Multi Line
        # CODE
        if block.startswith("```\n") and block.endswith("```"):
            return BlockType.CODE
        # QUOTE
        if block.startswith("> "):
            every_line = True
            lines = block.split("\n")
            for line in lines:
                if not line.startswith("> "):
                    every_line = False
            if every_line == True:
                return BlockType.QUOTE
        # UNORDERED LIST
        if block.startswith("- "):
            every_line = True
            lines = block.split("\n")
            for line in lines:
                if not line.startswith("- "):
                    every_line = False
            if every_line == True:
                return BlockType.UNORDERED_LIST
        # ORDERED LIST
        if block.startswith("1. "):
            every_line = True
            lines = block.split("\n")
            for i in range(0, len(lines)):
                line = lines[i]
                if not line.startswith(f"{i+1}. "):
                    every_line = False
            if every_line == True:
                return BlockType.ORDERED_LIST

    # Otherwise we are a normal paragraph
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    body = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.HEADING:
                parts = block.split()
                body.children.append(ParentNode(f"h{len(parts[0])}", text_to_children(parts[1])))
            case BlockType.CODE:
                parts = block.split("```\n")
                if len(parts) > 1:
                    pre = ParentNode("pre", [LeafNode("code", parts[1][:-3])])
                    body.children.append(pre)
                else:
                    pre = ParentNode("pre", [LeafNode("code", block)])
                    body.children.append(pre)
            case BlockType.QUOTE:
                body.children.append(ParentNode("blockquote", text_to_children(block)))
            case BlockType.UNORDERED_LIST:
                parts = block.split("\n")
                ul = ParentNode("ul", [])
                for part in parts:
                    ul.children.append(ParentNode("li", text_to_children(block[2:])))
            case BlockType.ORDERED_LIST:
                parts = block.split("\n")
                ol = ParentNode("ol", [])
                for part in parts:
                    ol.children.append(ParentNode("li", text_to_children(block[2:])))
            case BlockType.PARAGRAPH:
                text_no_new_lines = block.replace("\n", " ")
                body.children.append(ParentNode("p", text_to_children(text_no_new_lines)))


            case _:
                raise Exception("Idk what you are giving me, but stop")

    return body

def text_to_children(text):
    return list(map(lambda n: text_node_to_html_node(n), text_to_textnodes(text)))


