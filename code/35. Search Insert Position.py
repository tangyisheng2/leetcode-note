#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :35. Search Insert Position.py
# @Time      :11/5/21 1:18 AM
# @Author    :Eason Tang
from typing import List


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         lo = 0
#         hi = n - 1  # 定义target在左闭右闭的区间里，[left, right]
#         while lo <= hi:  # 当left==right，区间[left, right]依然有效
#             mid = (lo + hi) // 2
#             print(f"lo = {lo}, mid = {mid}, hi = {hi}, comparing {nums[mid]} and {target}")
#             if nums[mid] < target:
#                 lo = mid + 1  # target 在右区间，所以[middle + 1, right]
#             elif nums[mid] > target:
#                 hi = mid - 1  # target 在左区间，所以[left, middle - 1]
#             else:
#                 return mid  # nums[middle] == target
#         # 分别处理如下四种情况
#         # 目标值在数组所有元素之前  [0, -1], 此时跳出while，return hi + 1
#         # 目标值等于数组中某一个元素  return middle;
#         # 目标值插入数组中的位置 [left, right]，return  right + 1
#         # 目标值在数组所有元素之后的情况 [left, right]， return right + 1
#         return hi + 1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)  # 定义target在左闭右开的区间内 - [lo, hi)
        while lo < hi:  # 当lo == hi时，[lo, hi)是无效区间，因此用"<"
            mid = (lo + hi) // 2
            if nums[mid] > target:  # 当num[mid] > target，target应该在左区间[lo, hi]
                hi = mid
            elif nums[mid] < target:    # 当num[mid] < target, target应该在右区间[mid + 1, hi)
                lo = mid + 1
            else:   # nums[middle] == target
                return mid
            # // 分别处理如下四种情况
            # // 目标值在数组所有元素之前[0, 0)
            # // 目标值等于数组中某一个元素return middle
            # // 目标值插入数组中的位置[left, right) ，return right即可
            # // 目标值在数组所有元素之后的情况[left, right)，return right即可
        return hi





test = Solution()
ret = test.searchInsert([1, 3, 5, 6], 0)

