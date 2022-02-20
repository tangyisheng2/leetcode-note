#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1380. Lucky Numbers in a Matrix.py
# @Time      :2/14/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minRow = [min(row) for row in matrix]
        maxCol = [max(col) for col in zip(*matrix)]
        """
        zip(*matrix) = zip(matrix[0], matrix[1], matrix[2])
                     = [matrix[0][0], matrix[1][0], matrix[2][0]]
        相当于将原数组转置
        """
        ans = []
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == minRow[i] == maxCol[j]:
                    ans.append(x)
        return ans


test = Solution()
test.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]])
