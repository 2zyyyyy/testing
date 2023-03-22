
# class Dog:
#     def __init__(self, name):
#         self.name = name


# d = Dog('wangcai')
# # hasattr：判断对象是否有该属性
# print(hasattr(d, 'name'))
# print(hasattr(d, 'age'))

# locals
# def test():
#     print('before define a')
#     print(locals())
#     a = 1
#     print('after define a')
#     print(locals())

# test()

# staticmethod和classmethod
class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        """
        定义普通方法（至少需要一个 self 参数）
        """
        print(format(self.name), '{}会润')

    @classmethod
    def classMtthodDog(cls, x):
        """
        定义类方法：至少需要一个 cls 参数
        """
        print('Executing classDog({}, {})'.format(cls, x))

    @staticmethod
    def staticMethodDog(x):
        """
        定义静态方法：无默认参数
        """
        print('Executing staticMethodDOg({})'.format(x))
