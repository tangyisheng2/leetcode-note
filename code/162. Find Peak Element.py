# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   162. Find Peak Element.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List

#
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         local_max = nums[0]
#         i = 0
#         while i < len(nums):
#             if nums[i] >= local_max:  # 目前还在上升区间
#                 local_max = nums[i]
#             if nums[i] < local_max:  # 找到了第一个下降的元素，那么peak就是上一个
#                 return i - 1
#             if i == len(nums) - 1:  # 搜索到最后都没有答案，peak在数组边界
#                 return i
#             i += 1


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        lo, hi = 0, len(nums) - 1
        while lo < hi:  # 小于号
            mid = (lo + hi) // 2
            if nums[mid] <= nums[mid + 1]:
                lo = mid + 1    # lo一定+1
            else:
                hi = mid
        return lo

test = Solution()
test.findPeakElement([1])