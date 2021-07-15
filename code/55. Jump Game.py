# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   55. Jump Game.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         """
#         DP
#         :param nums:
#         :return:
#         """
#         if len(nums) == 1:  # 特殊情况：如果长度为1则可以直接到终点，返回true
#             return True
#
#         dp = [0 for _ in range(len(nums) + 1)]
#         dp[1] = 1
#         for i in range(1, len(nums) + 1):
#             if dp[i]:  # 如果当前dp可以达到
#                 for j in range(i, i + nums[i - 1] + 1):  # 注意dp表中idx比nums中idx多1，同时由于本题取闭区间，所以上界为i + nums[i - 1] + 1
#                     if j < len(nums):  # 在更新dp表的同时要注意数组是否越界，因为在这里我们取开区间，所以不用 + 1
#                         dp[j] = 1  # 当前dp的钱nums[i - 1]位都可以达到
#                     else:
#                         return True  # 剪枝，否则超时
#         return True if dp[-1] else False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        DP
        :param nums:
        :return:
        """
        if len(nums) == 1:  # 特殊情况：如果长度为1则可以直接到终点，返回true
            return True

        max_reachable_idx = 0
        for i in range(len(nums)):
            if i <= max_reachable_idx:  # 如果没有到目前可以跳到最远的尽头
                max_reachable_idx = max(max_reachable_idx, i + nums[i])  # 更新尽头
            else:
                return False

        return True
