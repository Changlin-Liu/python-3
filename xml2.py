# 操作XML有两种方法：DOM和SAX
# DOM会把整个XML读入内存，解析为树，因此占用内存大，有点是可以遍历树的任意节点。
# SAX是流模式，边读边解析，占用内存小，缺点是需要自己处理事件

from xml.parsers.expat import ParserCreate


class defaultHandler(object):

    def start_element(tag, attrs):  #start_element处理标签首部内容【 如<child1 name="paul">】
        print('Start element:', tag, attrs)

    def end_element(name):  #end_element处理标签尾部内容【</child1>】
        print('End element:', name)

    def char_data(data): #char_data处理正文部分【Text goes here】
        if data != '\n':
            print('Character data:', repr(data))


xml = """<?xml version="1.0" encoding="UTF-8"?>
<parent id="top" size="5">
    <child1 name="paul">Text goes here</child1>
    <child2 name="fred">More text</child2>
</parent>
"""
p = ParserCreate()
p.StartElementHandler = defaultHandler.start_element
p.EndElementHandler = defaultHandler.end_element
p.CharacterDataHandler = defaultHandler.char_data
p.Parse(xml)

