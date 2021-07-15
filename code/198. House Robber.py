# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   198. House Robber.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划：
        特殊情况1: 只有1间房子的时候直接抢
        特殊情况2: 有两间房子时，因为不能连续抢两间房子，因此选择价值高的抢
        子问题转换方程：
        抢前n间房子能获得的最大值 = 抢前n - 2间房子能获得的最大值和第n间房子的价值之和； 抢前n - 1间房子能获得的最大值（不抢第n间房子）两者的最大值
        :param nums:
        :return:
        """
        if len(nums) == 1:  # 特殊情况1
            return nums[0]
        if len(nums) == 2:  # 特殊情况2
            return max(nums[0], nums[1])

        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, n + 1):
            # 抢前n间房子能获得的最大值 = 抢前n - 2间房子能获得的最大值和第n间房子的价值之和； 抢前n - 1间房子能获得的最大值（不抢第n间房子）两者的最大值
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        return dp[-1]
