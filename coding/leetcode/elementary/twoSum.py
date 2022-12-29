""" 
梦开始的地方：两数之和
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


if __name__ == '__main__':
    n = [1, 3, 5, 7, 9, 10, 13]
    t = 10
    print(Solution().twoSum(nums=n, target=t))
