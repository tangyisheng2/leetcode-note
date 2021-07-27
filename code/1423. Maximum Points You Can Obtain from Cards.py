# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1423. Maximum Points You Can Obtain from Cards.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


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
