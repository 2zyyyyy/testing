from typing import List

# Bubble Sort(Python)
""" 冒泡排序(Bubble Sort)是经典排序算法之一，属于交换排序的一种，
基本的排序思路是：从头开始两两元素进行比较，大的元素就往上冒，
这样遍历一轮后，最大的元素就会直接筛选出来。然后再重复上述操作，
即可完成第二大元素的冒泡。以此类推，直到所有的元素排序完成 """


class Solution:
    def bubble_sort(self, nums: List[int]):
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


if __name__ == '__main__':
    nums = [46]
    print("初始数据：", nums)
    Solution().bubble_sort(nums)
    print("冒泡排序结果：", nums)
