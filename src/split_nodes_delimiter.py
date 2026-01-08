from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

    parts = node.text.split(delimiter)
    if len(parts) % 2 == 0:
        raise Exception("Invalid markdown syntax")

    for i in range(0, len(parts)):
        part = parts[i]

        if part == "":
            continue
            
        if i % 2 == 0:
            nodes.append(TextNode(part, TextType.TEXT))
        else:
            match delimiter:
                case "`":
                    nodes.append(TextNode(part, TextType.CODE))
                case "**":
                    nodes.append(TextNode(part, TextType.BOLD))
                case "_":
                    nodes.append(TextNode(part, TextType.ITALIC))

    return nodes