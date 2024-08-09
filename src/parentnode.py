from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None) -> None:
        self.value = None
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided!")
        if self.children is None:
            raise ValueError("No children provided!")

        html_string = f"<{self.tag}>"
        for child in self.children:
            if isinstance(child, LeafNode):
                html_string += child.to_html()
            else:
                html_string += child.to_html()

        return html_string + f"</{self.tag}>"
