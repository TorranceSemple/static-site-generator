class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children # list of htmlnode objects
        self.props = props # dict of attributes of a html tag
        
    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML")
    
    def props_to_html(self):
        if not self.props:
            return ""
        html_attributes = []
        for k,v in self.props.items():
            html_attributes.append(f'{k}="{v}"')
        return " " + " ".join(html_attributes)
    
    def __repr__(self):
        return f"HTMLNode tag={self.tag} value={self.value} children={len(self.children)} props={self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value 
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("No Tag.")
        if self.children is None:
            raise ValueError("No Children.")
        
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"
        childen_strings = ""
        
        for child in self.children:
            childen_strings += (child.to_html())
        
        return opening_tag + childen_strings + closing_tag
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"