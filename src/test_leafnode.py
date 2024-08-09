import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_has_no_child(self):
        leaf = LeafNode("p", "This is a paragraph of text", "b", None)
        self.assertIsNone(leaf.children)

    def test_no_tag(self):
        leaf = LeafNode(None, "This is text no tag")
        self.assertEqual(leaf.to_html(), "This is text no tag")

    def test_tag_with_props(self):
        test_props = {"href": "https://www.boot.dev", "target": "_blank"}
        leaf = LeafNode("a", "Link to BootDev", None, test_props)
        self.assertEqual(
            leaf.to_html(),
            '<a href="https://www.boot.dev" target="_blank">Link to BootDev</a>',
        )

    def test_tag_with_img(self):
        test_props = {"src": "https://placehold.co/200", "alt": "placeholder200x200"}
        leaf = LeafNode("img", None, None, test_props)
        self.assertEqual(
            leaf.to_html(),
            '<img src="https://placehold.co/200" alt="placeholder200x200">',
        )


if __name__ == "__main__":
    unittest.main()
