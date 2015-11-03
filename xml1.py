from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('start_element: %s, attrs: %s' % (name, str(attrs)))
    def end_element(self, name):
        print('end_element: %s' % name)
    def char_data(self, text):
        print('char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <a bref="/python">Python</a>
    <a bref="/ruby">ruby</a>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)