class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = ""
        if self.props is None or len(self.props) <= 0:
            return props_string

        for prop_key, prop_value in self.props.items():
            props_string += f'{prop_key}="{prop_value}" '
        return props_string.strip()

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
