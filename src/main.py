from textnode import TextNode, TextType

def main():
    test = TextNode("Google", TextType.LINK, "https://www.google.com")
    print(test)

if __name__ == "__main__":
    main()