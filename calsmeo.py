class foo(object):
    def f1(self):
        print('normal')
    @classmethod
    def f2(cls):
        print('class')
# foo_s1 = foo()
# print(foo_s1.f1())
print(foo.f2())