# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1277. Count Square Submatrices with All Ones.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                # f[i][j]是以坐标(i,j)为右下顶点的正方形数量，同时表示以(i,j)为右下角的正方形最大边长
                # 正方形以f[i][j]处边长为1的正方形逐渐向左上延伸
                if i == 0 or j == 0:  # 边界节点只有可能存在边长为1的正方形或不能构成正方形
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:  # 输入等于0的时候不存在
                    f[i][j] = 0
                else:
                    # 要左上方的3个正方形将所有格子都cover到，才能通过添加右下方的顶点组成边长更大的三角形
                    # 所以我们更新DP时取最小值
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans += f[i][j]
        return ans
