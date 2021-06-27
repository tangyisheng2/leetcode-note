#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :322. Coin Change.py
# @Time      :2021/6/28 12:22 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1 and coins[0] > amount:
            return -1

        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i + coin < len(dp) and dp[i] != -1:
                    if dp[i+coin] == -1:
                        dp[i + coin] = dp[i] + 1
                    else:
                        dp[i + coin] = min(dp[i] + 1, dp[i + coin])
        return dp[amount]


test = Solution()
ret = test.coinChange(coins=[2], amount=3)
print(ret)
