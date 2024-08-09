import unittest

from leafnode import LeafNode
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a another node", "bold")
        self.assertNotEqual(node, node2)

    def test_string_repr(self):
        node = TextNode("This is a test", "italic")
        self.assertEqual(repr(node), "TextNode(This is a test, italic, None)")

    def test_default_value_url(self):
        node = TextNode("This is a TextNode", "bold")
        self.assertIsNone(node.url)

    def test_url_value(self):
        node = TextNode("This is a TextNode", "bold", "https://www.boot.dev")
        self.assertEqual(node.url, "https://www.boot.dev")

    def test_text_to_leafnode(self):
        text = TextNode("This is a bold text", "bold")
        leaf = text.text_node_to_html_node()
        self.assertIsInstance(leaf, LeafNode)
        self.assertEqual(leaf.to_html(), "<b>This is a bold text</b>")


if __name__ == "__main__":
    unittest.main()
