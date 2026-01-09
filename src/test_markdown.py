import unittest

from markdown import *


class TestMarkdown(unittest.TestCase):    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_block_to_block_type(self):
        md = """
This is a paragraph.

# This is a heading 1

## This is a heading 2

###### This is a heading 6

```
This is a code block
```

> This is a quote
> From the great
> Leeeeeroy Jeeeeeenkins

- Wake up
- Go pee
- SCREAM
- Go pee
- Go to bed

1. You thought the last list was in order?
2. Amatuer
3. This list is in order, I'll pee whenever I want
4. Ain't gotta leave no bed for that
"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            block_to_block_type(blocks[0]),
            BlockType.PARAGRAPH
        )        
        self.assertEqual(
            block_to_block_type(blocks[1]),
            BlockType.HEADING
        )        
        self.assertEqual(
            block_to_block_type(blocks[2]),
            BlockType.HEADING
        )        
        self.assertEqual(
            block_to_block_type(blocks[3]),
            BlockType.HEADING
        )        
        self.assertEqual(
            block_to_block_type(blocks[4]),
            BlockType.CODE
        )        
        self.assertEqual(
            block_to_block_type(blocks[5]),
            BlockType.QUOTE
        )        
        self.assertEqual(
            block_to_block_type(blocks[6]),
            BlockType.UNORDERED_LIST
        )        
        self.assertEqual(
            block_to_block_type(blocks[7]),
            BlockType.ORDERED_LIST
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_simple_paragraph(self):
        md = "This is a simple paragraph"
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a simple paragraph</p></div>",
        )

if __name__ == "__main__":
    unittest.main()