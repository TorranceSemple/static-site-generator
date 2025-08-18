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