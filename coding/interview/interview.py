
import string


class InterView:
    # 题目：给定一个字符串，返回该字符串中出现次数最多的字符和次数
    def sumOfChars(self, str: string):
        # 使用字典存储传进来的字符串
        str_dict = {}
        if len(str) == 0:
            print("请输入长度大于0的字符串")
            return
        # 其中，我们使用字典存储每个字母出现的次数，并在循环中对每个字母进行计数
        for s in str:
            if s in str_dict:
                str_dict[s] += 1
            else:
                str_dict[s] = 1
            print(f'{str_dict}')
        # 最后使用 max() 函数取出字典中键值最大的字母，即出现次数最多的字母
        most_str = max(str_dict)
        print(f'最大值是：{most_str}, 出现了{str_dict[most_str]}次')


if __name__ == '__main__':
    InterView().sumOfChars("123344")
