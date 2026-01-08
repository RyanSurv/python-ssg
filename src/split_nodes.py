from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    # use `extract_markdown_links` to get all of the links
    # this will return tuples in the following format;
    # ("alt text", "url") i.e. ("image", "https://i.imgur.com/zjjcJKZ.png")
    # so we can then .split() each node.value at: [alt text] AS WELL AS (url)
    # to seperate them out into their own nodes (and have the remainders as text nodes)
    new_nodes = []

    for node in old_nodes:
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)

        links = extract_markdown_links(node.text)
        
        for link in links:
            parts = node.text.split(f"[{link[0]}]({link[1]})")
            if len(parts) < 1: # We done messed up a-aron
                print("Idk how we got here, this is not ideal man")
                break

            # Turn parts[0] into a TEXT node and append to new_nodes
            new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # Create and add a link node to new_nodes
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            # recursively check for links in parts[1]?

    def check_for_links(nodes, node):


    return new_nodes
