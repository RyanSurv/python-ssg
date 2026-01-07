class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")

    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return ""

        s = ""
        for key in self.props:
            s += f" {key}=\"{self.props[key]}\""
        return s

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf value must not be None")
        if self.tag == None:
            return str(value)

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent tag must not be None")
        if self.children == None:
            raise ValueError("Children must not be None")
        
        s = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            s += child.to_html()
        s += f"</{self.tag}>"
        return s