from enum import Enum

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