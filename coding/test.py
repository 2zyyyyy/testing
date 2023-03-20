
# class Dog:
#     def __init__(self, name):
#         self.name = name


# d = Dog('wangcai')
# # hasattr：判断对象是否有该属性
# print(hasattr(d, 'name'))
# print(hasattr(d, 'age'))

# locals
def test():
    print('before define a')
    print(locals())
    a = 1
    print('after define a')
    print(locals())

test()
