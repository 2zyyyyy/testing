def sortDict():
    dic = {'a':31,'d':4, 'b':5, 'c':3}
    # 根据 key 排序 [('a', 31), ('b', 5), ('c', 3), ('d', 4)]
    dict1 = sorted(dic.items(), key=lambda d:d[0])
    print(dict1)

    # 根据 value 排序(降序)  # [('a', 31), ('b', 5), ('d', 4), ('c', 3)]
    dict2 = sorted(dic.items(), key=lambda d:d[1], reverse=True)
    print(dict2)

    # 根据 value 排序(升序) [('c', 3), ('d', 4), ('b', 5), ('a', 31)]
    dict3 = sorted(dic.items(), key=lambda d:d[1]) 
    print(dict3)

# 求奇偶数（使用列表推导式）
def odd(num):
    return [x for x in range(num) if x % 2 == 1]

# 字符串整数列表转 int list
def strListToIntList():
    # 使用list&map&lambda
    strList = ['1', '20', '300', '4000']
    return list(map(lambda a: int(a), strList))

# 删除重复项
def delRepeatItem():
    num = [1, '2', 'c', 1, 'c', '2', 0]
    return list(set(num))

# 9 9 乘法表
def multiplication():
    # for king
    for i in range (1, 10):
        for j in range(1, i+1):
            print(f'{j}*{i}={i*j}\t', end='')
        print()   
    # 列表推导式
    # print('\n'.join([' '.join([f"{j}*{i}={i*j}" for j in range(1, i+1)]) for i in range(1, 10)]))

 # 找相同&&找不同
def findElement():
    a = [1, 2, '123', '点击', 100, 'find'] 
    b = [2, 1, '456', 100, '点击一次', 'find']  
    # 找相同
    print(set(a) & set(b))
    # 找不同
    print(set(a) ^ set(b))

# 列表生成器
def bulider():
    a = [1, 3, 5, 7, 9]
    # 方法 1
    # for i in range (len(a)):
    #     a[i] += 1
    # print(a)

    # 方法 2
    # a = map(lambda x:x+1, a)
    # for i in a:
    #     print(i)

if __name__ == '__main__':
    # sortDict()
    # print(odd(10))
    # print(strListToIntList())
    # print(delRepeatItem())
    # multiplication()
    # findElement()
    bulider()
