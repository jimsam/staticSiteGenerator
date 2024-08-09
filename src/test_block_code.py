import unittest

from block_code import block_to_block_type, markdown_to_blocks, markdown_to_html_node


class TestBlockCode(unittest.TestCase):
    maxDiff = None

    def test_markdown_to_html_node(self):
        block_str = """# This is a heading

                       ## This a heading 2

                       This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                       ``` print("This is a test") ```

                       > This is a quote of text. It has some **bold** and *italic* words inside of it.

                       1. This is ol 1
                       2. This is ol 2

                       * This is ul 1 
                       * This is ul 2
                       * This is ul 3"""
        expected_string = """<div><h1>This is a heading</h1><h2>This a heading 2</h2><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><code> print("This is a test") </code><blockquote>This is a quote of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</blockquote><ol><li>This is ol 1</li><li>This is ol 2</li></ol><ul><li>This is ul 1</li><li>This is ul 2</li><li>This is ul 3</li></ul></div>"""
        resulted_string = markdown_to_html_node(block_str)
        self.assertEqual(resulted_string, expected_string)

    def test_markdown_to_html_node_quote(self):
        block_str = """
> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.
> I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.
> I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author."""
        expected_string = """<div><blockquote>"I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.</blockquote><blockquote>I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.</blockquote><blockquote>I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author.</blockquote></div>"""
        resulted_string = markdown_to_html_node(block_str)
        self.assertEqual(resulted_string, expected_string)

    def test_markdown_to_blocks(self):
        block_str = """# This is a heading

                       This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                       ``` print("This is a test") ```

                       * This is the first list item in a list block
                       * This is a list item
                       * This is another list item"""
        block_list = markdown_to_blocks(block_str)
        self.assertEqual(
            block_list,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                '``` print("This is a test") ```',
                """* This is the first list item in a list block
* This is a list item
* This is another list item""",
            ],
        )

    def test_block_to_block_type_paragraph(self):
        str_to_match = "# This is a heading"
        type_of_block = block_to_block_type(str_to_match)
        self.assertEqual(type_of_block, "heading")

    def test_block_to_block_type_code(self):
        str_to_match = "``` print('this is code')```"
        type_of_block = block_to_block_type(str_to_match)
        self.assertEqual(type_of_block, "code")

    def test_block_to_block_type_quote(self):
        str_to_match = """> This is a quote line 1
>This is quote line 2"""
        type_of_block = block_to_block_type(str_to_match)
        self.assertEqual(type_of_block, "quote")

    def test_block_to_block_type_unordered_list(self):
        str_to_match = """* This is a unordered line 1
* This is unordered list 2"""
        type_of_block = block_to_block_type(str_to_match)
        self.assertEqual(type_of_block, "unordered_list")

    def test_block_to_block_type_ordered_list(self):
        str_to_match = """1. This is a ordered list 1
2. This is ordered list 2"""
        type_of_block = block_to_block_type(str_to_match)
        self.assertEqual(type_of_block, "ordered_list")


if __name__ == "__main__":
    unittest.main()
