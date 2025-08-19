import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_HTML(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
        self.assertNotEqual(node.props_to_html(),'href="https://www.google.com" target="_blank"')
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    def test_to_html_with_grandchildren_and_url(self):
        grandchild_node = LeafNode("a", "Click here", {"href": "https://www.google.com", "target": "_blank"})
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        
        expected = '<div><p><a href="https://www.google.com" target="_blank">Click here</a></p></div>'
        self.assertEqual(parent_node.to_html(), expected)
    
if __name__ == "__main__":
    unittest.main()