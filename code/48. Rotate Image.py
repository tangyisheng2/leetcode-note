#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :48. Rotate Image.py
# @Time      :4/11/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp
