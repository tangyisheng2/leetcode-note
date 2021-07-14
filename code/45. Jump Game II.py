# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   45. Jump Game II.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import math
from typing import List


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         """ 贪心策略解题 """
#         """
#         n 长度
#         step 步长
#         left ，right  当前位置元素能到达的第一个元素和最后一个元素
#         cur 当前位置的元素
#         """
#         n = len(nums)
#         step = 0
#         cur = 0
#
#         if n == 1:
#             return 0
#
#         while cur < n:
#
#             lo = cur + 1
#             hi = cur + nums[cur]
#             if hi >= n - 1:  # 下一跳可以跳到终点
#                 return step + 1
#             tmp_max = 0
#             for i in range(lo, hi + 1):
#                 if i + nums[i] > tmp_max:
#                     cur = i  # 跳到下一跳允许距离最长的点
#                     tmp_max = nums[i] + i
#             step += 1  # 准备起跳

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(len(nums) + 1)]
        for i in range(1, n):
            for j in range(i, i + nums[i - 1] + 1):
                if j < len(dp):
                    if dp[j] == 0:
                        dp[j] = dp[i] + 1
                    else:
                        dp[j] = min(dp[i] + 1, dp[j])
        return dp[n] - 1  # todo 为什么-1


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0 for _ in range(n + 1)]
#         j = 0
#         for i in range(n):
#             while j + nums[j] < i:
#                 j += 1
#             dp[i] = dp[j] + 1
#         return dp[n-1]


test = Solution()
ret = test.jump(
    [1, 1, 1, 1])
print(ret)
