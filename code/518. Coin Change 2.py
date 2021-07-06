# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   518. Coin Change 2.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng

@Modify Time        @Author     @Version        @Description
------------        -------     --------        -----------
2021/7/7     tangyisheng2        1.0             数据库链接
"""
from typing import List


# class Solution:
#     def __init__(self):
#         self.ans = 0
#         self.change_result = set()
#         self.memo = {}
#
#     def change_memorize(self, amount: int, coins: List[int]) -> int:
#         if amount == 0:
#             return []
#         if min(coins) > amount:
#             return 0
#
#         for coin in coins:
#             remainder = amount - coin
#             remainder_result = self.change_memorize(remainder, coins)
#             if remainder_result:
#                 self.ans += 1
#         return self.ans // amount
#
#     def change(self, amount: int, coins: List[int]) -> int:
#         self.memo = {}
#         return self.change_memorize(amount, coins)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-iihe-pa-lou-ti-wen-ti-dao-di-yo/
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:  # 注意这两个循环嵌套顺序不同导致求得的结果不同（组合数，排列数
            for i in range(len(dp)):
                if i + coin < len(dp):
                    dp[i + coin] += 1
        return dp[amount] + 1


test = Solution()
ret = test.change(amount=5, coins=[1, 2, 5])
print(ret)
