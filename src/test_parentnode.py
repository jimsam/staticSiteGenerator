import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_leafnode_to_html(self):
        leaf_list = [
            LeafNode("p", "This is the first paragraph"),
            LeafNode("p", "This is the second paragraph"),
        ]
        parent = ParentNode("div", leaf_list)
        self.assertEqual(
            parent.to_html(),
            "<div><p>This is the first paragraph</p><p>This is the second paragraph</p></div>",
        )

    def test_parentnode_to_html(self):
        parent_list = [ParentNode("p", [])]
        parent = ParentNode("div", parent_list)
        self.assertEqual(parent.to_html(), "<div><p></p></div>")

    def test_mixnodes_to_html(self):
        mixed_list = [
            LeafNode("h1", "This is a header 1"),
            ParentNode(
                "div",
                [
                    LeafNode("p", "This is the first paragraph"),
                    LeafNode("p", "This is the second paragraph"),
                ],
            ),
            LeafNode("h2", "This is a header 2"),
        ]
        parent = ParentNode("div", mixed_list)
        self.assertEqual(
            parent.to_html(),
            "<div><h1>This is a header 1</h1><div><p>This is the first paragraph</p><p>This is the second paragraph</p></div><h2>This is a header 2</h2></div>",
        )

    def test_parentnode_no_tag(self):
        leaf_list = [
            LeafNode("b", "This is"),
            LeafNode(None, " normal text."),
        ]
        parent = ParentNode("div", leaf_list)
        self.assertEqual(parent.to_html(), "<div><b>This is</b> normal text.</div>")


if __name__ == "__main__":
    unittest.main()
