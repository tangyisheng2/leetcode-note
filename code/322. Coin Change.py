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
                    if dp[i + coin] == -1:
                        dp[i + coin] = dp[i] + 1
                    else:
                        dp[i + coin] = min(dp[i] + 1, dp[i + coin])
        return dp[amount]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        # def dp(rem) -> int:
        #     if rem < 0: return -1
        #     if rem == 0: return 0
        #     mini = int(1e9)
        #     for coin in coins:
        #         res = dp(rem - coin)
        #         if res >= 0 and res < mini:
        #             mini = res + 1
        #     return mini if mini < int(1e9) else -1

        # if amount < 1: return 0
        # return dp(amount)

        def solve(remainder, cnt):
            nonlocal ans
            if remainder < 0:
                return

            if remainder == 0:
                ans = min(ans, cnt)
                return

            for coin in coins:
                solve(remainder - coin, cnt + 1)

        ans = int(1e9)
        coins.sort(reverse=True)
        solve(amount, 0)

        return ans


test = Solution()
ret = test.coinChange2(coins=[1, 2, 5], amount=11)
print(ret)
