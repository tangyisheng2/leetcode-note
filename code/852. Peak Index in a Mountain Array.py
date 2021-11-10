#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :852. Peak Index in a Mountain Array.py
# @Time      :11/9/21 6:15 PM
# @Author    :Eason Tang
from typing import List


# class Solution:
#     # Linear Solution
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         for i in range(1, len(arr)):
#             if arr[i - 1] > arr[i]:
#                 return i - 1
#         return "-1"


# class Solution:
#     # Binary Search
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         lo = 0
#         hi = len(arr) - 1
#         ans = 0
#
#         while lo <= hi:
#             mid = (lo + hi) // 2
#             if arr[mid] > arr[mid + 1]:
#                 ans = mid
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return ans


class Solution:
    def peakIndexInMountainArray(self, arr):
        l, r = 0, len(arr)
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] > arr[m + 1]:
                r = m - 1
            else:
                l = m + 1
        return l


test = Solution()
ret = test.peakIndexInMountainArray(arr=[24, 69, 100, 99, 79, 78, 67, 36, 26, 19])
print(ret)
