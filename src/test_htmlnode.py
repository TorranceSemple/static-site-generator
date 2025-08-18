import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_HTML(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
        self.assertNotEqual(node.props_to_html(),'href="https://www.google.com" target="_blank"')
    
if __name__ == "__main__":
    unittest.main()