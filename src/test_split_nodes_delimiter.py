import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiterNode(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("Hello **world**!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ])

    def test_split_italic(self):
        node = TextNode("Hello _world_!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.ITALIC),
            TextNode("!", TextType.TEXT),
        ])

    def test_split_code(self):
        node = TextNode("Hello `fmt.Println('go supremecy')` because Go is best!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("fmt.Println('go supremecy')", TextType.CODE),
            TextNode(" because Go is best!", TextType.TEXT),
        ])    
        
    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()