
class Dog:
    def __init__(self, name):
        self.name = name


d = Dog('wangcai')
# hasattr：判断对象是否有该属性
print(hasattr(d, 'name'))
print(hasattr(d, 'age'))
