import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("b", "great_grandchild")
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><span><b>great_grandchild</b></span></p></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(
            parent_node.to_html(),
            "<div></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node_a = LeafNode("b", "child_a")
        child_node_b = LeafNode("b", "child_b")
        child_node_c = LeafNode("b", "child_c")
        parent_node = ParentNode("div", [child_node_a, child_node_b, child_node_c])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child_a</b><b>child_b</b><b>child_c</b></div>",
        )


if __name__ == "__main__":
    unittest.main()