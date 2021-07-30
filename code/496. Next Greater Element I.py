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
        """
        使用单调递增栈针对next greater elements问题
        也只有这个问题能被针对
        :param nums1:
        :param nums2:
        :return:
        """
        stack = []  # 单调递增栈（从栈顶到栈底单调递增）
        hashmap = {}  # 存放结果的哈希表
        res = [-1] * len(nums1)  # 在没有找到结果（没有比他更大的数）的时候，默认值-1
        for i, num in enumerate(nums2):
            while stack and stack[-1][1] < num:  # 当前元素大于栈顶，表示下一个更大的元素找到了
                pre_i, _ = stack.pop()
                hashmap[pre_i] = (i, num)
            stack.append((i, num))  # 当前元素入栈

        # while stack:
        #     i, num = stack.pop()
        #     hashmap[i] = -1

        for i in range(len(nums1)):
            if nums2.index(nums1[i]) in hashmap:  # 检查有没有结果（有没有找到更大的元素）
                res[i] = hashmap[nums2.index(nums1[i])][1]  # 有就更新结果

        return res


if __name__ == '__main__':
    ret = Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4])
