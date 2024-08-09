import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        htmlnode = HTMLNode("p", "This is a paragraph")
        self.assertEqual(repr(htmlnode), "HTMLNode(p, This is a paragraph, None, None)")

    def test_properties_to_html(self):
        props_dict = {"href": "https://www.boot.dev", "target": "_blank"}
        htmlnode = HTMLNode("p", "This is a paragraph", None, props_dict)
        self.assertEqual(
            htmlnode.props_to_html(), 'href="https://www.boot.dev" target="_blank"'
        )

    def test_properties_to_html_no_props(self):
        htmlnode = HTMLNode("p", "This is a paragraph")
        self.assertEqual(htmlnode.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
