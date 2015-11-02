# from collections import deque
# q = deque([1, 2, 3])
# q.appendleft(4)
# q.pop()
# print(q)
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])
# from collections import OrderedDict
# od = OrderedDict()
# od['a'] = 4
# od['b'] = 1
# od['c'] = 2
# # print(od)
# for k, v in od.items():
#     print(k, ":", v)
from collections import Counter
c = Counter('abcdfcad')
print(c.most_common())