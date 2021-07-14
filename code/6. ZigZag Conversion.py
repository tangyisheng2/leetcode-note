# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6. ZigZag Conversion.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         """
#
#         :param s: 原来的字符串
#         :param numRows: 进行zigzag变换的行数
#         :return: zigzag变幻后的字符串
#         """
#         if numRows == 1 or numRows > len(s) - 1:   # 如果行数和列数少于s的长度，则直接返回
#             return s
#         arr = [[] for _ in range(numRows)]
#         moveDirection = True  # True向下，False向上
#         rowNum = 0
#         ret = ""
#         for ch in s:
#             arr[rowNum].append(ch)
#             if moveDirection:
#                 rowNum += 1
#             else:
#                 rowNum -= 1
#             if rowNum == 0 or rowNum == len(arr) - 1:
#                 moveDirection = not moveDirection  # 变换方向
#         for row in arr:
#             ret = f'{ret}{"".join(row)}'
#         return ret

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """

        :param s: 原来的字符串
        :param numRows: 进行zigzag变换的行数
        :return: zigzag变幻后的字符串
        """
        if numRows == 1 or numRows > len(s) - 1:   # 如果行数和列数少于s的长度，则直接返回
            return s
        ret = ""
        cycle_len = 2 * numRows - 2
        for i in range(numRows):
            k = 0
            while k * cycle_len + i < len(s):
                ret = f'{ret}{s[k * cycle_len + i]}'
                if i != 0 and i != numRows - 1 and \
                        (k + 1) * cycle_len - i < len(s):
                    ret = f'{ret}{s[(k + 1) * cycle_len - i]}'  # 如果非头尾两行有多一个元素
                k += 1
        return ret


test = Solution()
test.convert(s="PAYPALISHIRING", numRows=3)
