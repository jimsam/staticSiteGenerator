import unittest

from generator import extract_title, generate_page


class TestGenerator(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# BootDev")
        self.assertEqual(title, "BootDev")

    def test_extract_title_no_present(self):
        with self.assertRaises(ValueError):
            extract_title("BootDev")

    def test_generate_page(self):
        generate_page("context/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    unittest.main()
