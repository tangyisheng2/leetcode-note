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
#         self.ans = []
#         self.change_result = set()
#         self.memo = {}
#
#     def change_memorize(self, amount: int, coins: List[int]):
#         """
#
#         :param amount:
#         :param coins:
#         :return: Solution列表
#         """
#         if amount == 0:
#             return []
#         if min(coins) > amount or amount < 0:
#             return None
#
#         for coin in coins:
#             remainder = amount - coin
#             remainder_result = self.change_memorize(remainder, coins)
#             if remainder_result is not None:
#                 for solution in remainder_result:
#                     solution.append(coin)
#             pass
#         pass
#
#     def change(self, amount: int, coins: List[int]) -> int:
#         self.memo = {}
#         return self.change_memorize(amount, coins)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-iihe-pa-lou-ti-wen-ti-dao-di-yo/
        # problem(k,i) = problem(k-1, i) + problem(k, i-k) 即前 k 个硬币凑齐金额 i 的组合数 等于 前 k-1 个硬币凑齐金额 i 的组合数 加上 在原来 i-k
        # 的基础上使用硬币的组合数。说的更加直白一点，那就是用前 k 的硬币凑齐金额 i ，要分为两种情况开率，一种是没有用前 k-1 个硬币就凑齐了，一种是前面已经凑到了 i-k ，现在就差第 k 个硬币了。

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:  # 注意这两个循环嵌套顺序不同导致求得的结果不同（组合数，排列数
            for i in range(len(dp)):
                if i + coin < len(dp):
                    dp[i + coin] = dp[i] + dp[i + coin] # 不使用这个coin凑齐的办法个数与使用这个coin凑齐的办法个数
        return dp[amount]


test = Solution()
ret = test.change(amount=5, coins=[1, 2, 5])
print(ret)
