# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1423. Maximum Points You Can Obtain from Cards.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


# class Solution(object):
#     “”“
#     DFS暴力解法（超时）
#     """
#     def maxScore(self, cardPoints, k):
#         """
#         :type cardPoints: List[int]
#         :type k: int
#         :rtype: int
#         """
#         N = len(cardPoints)
#         self.memo = {}
#         return self.dfs(cardPoints, 0, N - 1, k)
#
#     def dfs(self, cardPoints, i, j, k):
#         if k == 0:
#             return 0
#         if (i, j) in self.memo:
#             return self.memo[(i, j)]
#         removeLeft = cardPoints[i] + self.dfs(cardPoints, i + 1, j, k - 1)
#         removeRight = cardPoints[j] + self.dfs(cardPoints, i, j - 1, k - 1)
#         res = max(removeLeft, removeRight)
#         self.memo[(i, j)] = res
#         return res


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        滑动窗口
        """
        n = len(cardPoints)
        presum_arr = [0] * (n + 1)
        for i in range(n):
            presum_arr[i + 1] = presum_arr[i] + cardPoints[i]
        res = float("inf")
        window_size = n - k
        for i in range(k + 1):  # 从窗口开始进行计算
            res = min(res, presum_arr[window_size + i] - presum_arr[i])
        return presum_arr[n] - res


if __name__ == '__main__':
    test = Solution()
    test.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3)
