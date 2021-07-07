# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   344. Reverse String.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         # reverse方法
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s.reverse()


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         # 指针法
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         i, j = 0, len(s) - 1
#         while i < j:
#             tmp = s[i]
#             s[i] = s[j]
#             s[j] = tmp
#             i += 1
#             j -= 1


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 堆栈
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for ch in s:
            stack.append(ch)
        s = []
        while stack:
            s.append(stack.pop())
        pass


test = Solution()
test.reverseString(s=["h", "e", "l", "l", "o"])
