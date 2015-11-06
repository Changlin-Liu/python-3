from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        # if tag == "a":
            # if len(attrs) == 0:
                # pass
            # else:
        for variable, value in attrs:
            if variable == "bref":
                self.links.append(value)


if __name__ == "__main__":
    html_code = """<a bref="www.google.com">google.com</a>
    <a bref="www.pythonclub.org">Pythonclub</a>"""
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    print(hp.links)