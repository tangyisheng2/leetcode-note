# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   496. Next Greater Element I.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         stack = []
#         hashmap = {}
#         res = [-1] * len(nums1)
#         for i, num in enumerate(nums2):
#             while stack and stack[-1][1] < num:
#                 pre_i, _ = stack.pop()
#                 hashmap[pre_i] = (i, num)
#             stack.append((i, num))
#
#         # while stack:
#         #     i, num = stack.pop()
#         #     hashmap[i] = -1
#
#         for i in range(len(nums1)):
#             if nums2.index(nums1[i]) in hashmap:
#                 res[i] = hashmap[nums2.index(nums1[i])][1]
#
#         return res

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        res = [-1] * len(nums1)
        for i, num in enumerate(nums2):
            while stack and stack[-1][1] < num:
                pre_i, _ = stack.pop()
                hashmap[pre_i] = (i, num)
            stack.append((i, num))

        # while stack:
        #     i, num = stack.pop()
        #     hashmap[i] = -1

        for i in range(len(nums1)):
            if nums2.index(nums1[i]) in hashmap:
                res[i] = hashmap[nums2.index(nums1[i])][1]

        return res


if __name__ == '__main__':
    ret = Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4])
