import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_p_eq(self):
        node = HTMLNode("p", "lorem ipsum")
        node2 = HTMLNode("p", "lorem ipsum")
        self.assertEqual(node, node2)

    def test_p_not_eq(self):
        node = HTMLNode("p", "lorem ipsum")
        node2 = HTMLNode("p", "do re mi")
        self.assertNotEqual(node, node2)

    def test_p_children_and_props_eq(self):
        node = HTMLNode("p", "lorem ipsum", [], {"_foo": "bar"})
        node2 = HTMLNode("p", "do re mi", [], {"_foo": "bar"})
        self.assertNotEqual(node, node2)

    def test_diff_nodes_not_eq(self):
        node = HTMLNode("p", "lorem ipsum", [], {"_foo": "bar"})
        node2 = HTMLNode("h1", "lorem ipsum", [], {"_foo": "bar"})
        self.assertNotEqual(node, node2)

    def test_props_to_html_eq(self):
        node = HTMLNode("p", "lorem ipsum", [], {"_foo": "bar"})
        node2 = HTMLNode("h1", "lorem ipsum", [], {"_foo": "bar"})

        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_props_to_html_not_eq(self):
        node = HTMLNode("p", "lorem ipsum", [], {"_foo": "bar"})
        node2 = HTMLNode("h1", "lorem ipsum", [], {"_bar": "baz"})

        self.assertNotEqual(node.props_to_html(), node2.props_to_html())


if __name__ == "__main__":
    unittest.main()