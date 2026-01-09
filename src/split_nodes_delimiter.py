from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        split_nodes = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax")

        for i in range(0, len(parts)):
            part = parts[i]

            if part == "":
                continue
                
            if i % 2 == 0:
                split_nodes.append(TextNode(part, TextType.TEXT))
            else:
                match delimiter:
                    case "`":
                        split_nodes.append(TextNode(part, TextType.CODE))
                    case "**":
                        split_nodes.append(TextNode(part, TextType.BOLD))
                    case "_":
                        split_nodes.append(TextNode(part, TextType.ITALIC))
        nodes.extend(split_nodes)

    return nodes