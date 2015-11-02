from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
# print(p.x)
if p is tuple:
    print('Ok')
else:
    print('No')