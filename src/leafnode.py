from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None and self.tag != "img":
            raise ValueError("LeafNode without value")
        elif self.tag is None:
            return self.value
        else:
            if self.tag == "img":
                return self.open_tag()
            return self.open_tag() + self.value + self.close_tag()

    def open_tag(self):
        tag_props = self.props_to_html()
        if tag_props == "":
            return f"<{self.tag}>"
        return f"<{self.tag} {tag_props}>"

    def close_tag(self):
        return f"</{self.tag}>"
