from html.parser import HTMLParser


class myHtmlParser(HTMLParser):

    def __init__(self):
        # 子类添加新属性，需要先调用父类进行初始化
        # HTMLParser.__init__(self)
        super(myHtmlParser, self).__init__()
        # 如果没有self前缀，则属性是局部的，方法结束则属性也结束
        self.flag = None

    # 处理<!开头的内容
    def handle_decl(self, decl):
        print('Encounter some declaration: ', decl)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.flag = 'a'
            for href, link in attrs:
                print('href:', link)
        else:
            print('Encounter the begging of tag: ', tag)

    def handle_data(self, data):
        if self.flag == 'a':
            print('data: ', data)

    def handle_endtag(self, tag):
        print('Encounter the end of tag: ', tag)

    # 处理注释
    def handle_comment(self, comment):
        print('Encounter some comments: ', comment)

html_detail = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\
 "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head><!--insert javaScript here!-->
    <title>
        test
    </title>
    <body>
        <a href="http://www.163.com">
            链接到163
        </a>
    </body>
</html>
"""


if __name__ == '__main__':
    m = myHtmlParser()
    m.feed(html_detail)
    m.close()
