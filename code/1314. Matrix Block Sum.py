# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1314. Matrix Block Sum.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
#         """
#         [
#             [1,2,3],
#             [4,5,6],
#             [7,8,9]
#         ]
#         """
#         m = len(mat)
#         n = len(mat[0])
#         ans = [[0 for _ in range(n)] for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 sum_res = 0
#                 for ii in range(max(0, i - k), min(m, i + k + 1)):
#                     for jj in range(max(0, j - k), min(n, j + k + 1)):
#                         sum_res += mat[ii][jj]
#                 ans[i][j] = sum_res
#         return ans

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        """
        m = len(mat)
        n = len(mat[0])
        sum_prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_prefix[i][j] = sum_prefix[i - 1][j] + sum_prefix[i][j - 1] - sum_prefix[i - 1][j - 1] + mat[i][j]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return sum_prefix[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) - get(i + k + 1, j - k) + get(i - k,
                                                                                                            j - k);
        return ans

if __name__ == '__main__':
    test = Solution()
    test.matrixBlockSum(mat=[[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]], k=3)
