'''import hashlib
# md5 = hashlib.md5()
# md5.update(b'how to use python')
# print(md5.hexdigest())
user = 'hejingqi'
password = '123456'
salt = 'qwerfvcxz'
sha1 = hashlib.sha1()
sha1.update((user + password + salt).encode('utf-8'))
print(sha1.hexdigest())
'''
import itertools
for key, group in itertools.groupby('AaaBBbcCAAa',\
 lambda c: c.upper()):
    print(key,list(group))