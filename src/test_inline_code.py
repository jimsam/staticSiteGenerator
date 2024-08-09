import unittest

from inline_code import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes,
)
from textnode import TextNode


class TestInlideNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_list = split_nodes_delimiter([node], "`", "code")
        correct_list = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_list, correct_list)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a *italic block* word", "text")
        new_list = split_nodes_delimiter([node], "*", "italic")
        correct_list = [
            TextNode("This is text with a ", "text"),
            TextNode("italic block", "italic"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_list, correct_list)

    def test_split_nodes_delimiter_with_multiple1(self):
        node = TextNode("This is text with a `code block` word and **bold**", "text")
        new_list = split_nodes_delimiter([node], "`", "code")
        correct_list = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word and **bold**", "text"),
        ]
        self.assertEqual(new_list, correct_list)

    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        new_tuple = extract_markdown_images(text)
        correct_tuple = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(new_tuple, correct_tuple)

    def test_markdow_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        new_tuple = extract_markdown_links(text)
        correct_tuple = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_tuple, correct_tuple)

    def test_split_node_links(self):
        text = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        new_list = split_nodes_links([text])
        correct_list = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_list, correct_list)

    def test_split_node_images(self):
        text = TextNode(
            "This is text with images ![400x400](https://placehold.co/400) and ![200x200](https://placehold.co/200)",
            "text",
        )
        new_list = split_nodes_images([text])
        correct_list = [
            TextNode("This is text with images ", "text"),
            TextNode("400x400", "image", "https://placehold.co/400"),
            TextNode(" and ", "text"),
            TextNode("200x200", "image", "https://placehold.co/200"),
        ]
        self.assertEqual(new_list, correct_list)

    def test_empty_split_node_images(self):
        text = TextNode("This is a string with no images", "text")
        new_list = split_nodes_images([text])
        correct_list = [TextNode("This is a string with no images", "text")]
        self.assertEqual(new_list, correct_list)

    def test_link_split_node_images(self):
        text = TextNode("This is a string with a [link](https:://boot.dev)", "text")
        new_list = split_nodes_images([text])
        correct_list = [
            TextNode("This is a string with a [link](https:://boot.dev)", "text")
        ]
        self.assertEqual(new_list, correct_list)

    def test_complex_split_node_images(self):
        text = TextNode(
            "This is the complex **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            "text",
        )
        new_list = split_nodes_images([text])
        correct_list = [
            TextNode(
                "This is the complex **text** with an *italic* word and a `code block` and an ",
                "text",
            ),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a [link](https://boot.dev)", "text"),
        ]
        self.assertEqual(new_list, correct_list)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        textnode_list = text_to_textnodes(text)
        correct_list = [
            TextNode("This is ", "text", None),
            TextNode("text", "bold", None),
            TextNode(" with an ", "text", None),
            TextNode("italic", "italic", None),
            TextNode(" word and a ", "text", None),
            TextNode("code block", "code", None),
            TextNode(" and an ", "text", None),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text", None),
            TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(textnode_list, correct_list)


if __name__ == "__main__":
    unittest.main()
