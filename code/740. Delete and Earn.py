#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :740. Delete and Earn.py
# @Time      :2021/6/22 1:50 PM
# @Author    :Eason Tang
import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        删除n，则数值为[n + 1]和[n - 1]的也会被删除
        strategy：
        1. 删除数量最多的元素n
        2. 如果数量最多，则删除最大的元素（？
        :param nums:
        :return:
        """
        counter = collections.Counter(nums)
        nums_count = [0] * (max(nums) + 1)
        for key in counter.keys():
            nums_count[key] = counter[key]

        dp = [0] * len(nums_count)

        dp[0] = 0   # DP 0特殊状况，不减去求任何东西一共有0积分
        dp[1] = max(nums_count[0] * 0, nums_count[1] * 1)   # 只有两个房子的情况下，偷价值较高的

        for i in range(2, len(nums_count)):
            """
            当超过2个房子的时候，有两种处理方式
            1. 不偷当前房子，则目前能获得的最高积分是n - 1个房子的积分
            2. 偷当前房子，由于相邻房子不能偷，因此可以获得的最大积分是n - 2个房子最大的积分+当前房子的积分
            """
            dp[i] = max(dp[i - 2] + nums_count[i] * i, dp[i - 1])

        return dp[-1]


test = Solution()
test.deleteAndEarn(nums=[3, 4, 2])

