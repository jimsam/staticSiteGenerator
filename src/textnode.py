from leafnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value) -> bool:
        return (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        match self.text_type:
            case "bold":
                return LeafNode("b", self.text)
            case "italic":
                return LeafNode("i", self.text)
            case "code":
                return LeafNode("code", self.text)
            case "link":
                return LeafNode("a", self.text, None, {"href": self.url})
            case "image":
                return LeafNode("img", None, None, {"src": self.url, "alt": self.text})
            case "paragraph":
                return LeafNode("p", self.text)
            case "list-item":
                return LeafNode("li", self.text)
            case _:
                return LeafNode(None, self.text)
