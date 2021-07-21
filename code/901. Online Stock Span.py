# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   901. Online Stock Span.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


# class StockSpanner:
#     # 暴力解法
#     def __init__(self):
#         self.stock_price = []
#         self.spam = [0]
#
#     def next(self, price: int) -> int:
#         self.stock_price.append(price)
#         self.spam.append(self.calSpam(price))
#         return self.spam[-1]
#
#     def calSpam(self, target):
#         cnt = 0
#         for i in reversed(range(len(self.stock_price))):
#             if self.stock_price[i] <= target:
#                 cnt += 1
#             else:
#                 return cnt
#         return cnt

# class StockSpanner(object):
#
#     def __init__(self):
#
#         self.prices = []  # 股票价格
#         self.dp = []  # DP
#         self.i = 0  # 当前的下标
#
#     def next(self, price):
#         if self.i == 0 or self.prices[-1] > price:  # 如果刚一开始添加数字或者此时的数字小于前一天的数字，就返回1
#             self.dp.append(1)
#         else:  # 否则就使用动态规划
#             j = self.i - 1
#             while j >= 0 and price >= self.prices[j]:  # 如当前数字为85，85>75，小于75的有连续4天，我直接跨到4天前看看是否小于85就可以了。
#                 j -= self.dp[j]  # 减去跨度
#             self.dp.append(self.i - j)
#         self.i += 1
#         self.prices.append(price)
#         return self.dp[-1]

# class StockSpanner(object):
#     def __init__(self):
#         self.prices = []  # （股票价格，跨度）
#
#     def next(self, price):
#         if not self.prices or self.prices[-1][0] > price:  # 如果刚一开始添加数字或者此时的数字小于前一天的数字，就返回1
#             self.prices.append((price, 1))
#         else:
#             spam = 1
#             last_price, last_price_spam = self.prices[-1]
#             while last_price <= price:
#                 spam += last_price_spam
#                 self.prices.pop()
#                 if self.prices:
#                     last_price, last_price_spam = self.prices[-1]
#                 else:
#                     break
#             self.prices.append((price, spam))
#         return self.prices[-1][1]

class StockSpanner(object):
    def __init__(self):
        self.stack = []  # （股票价格，跨度）

    def next(self, price):
        spam = 1  # 默认情况下跨度为1
        while self.stack and self.stack[-1][0] <= price:
            spam += self.stack.pop()[1]  # pop最后一个元素，spam + 1
        self.stack.append((price, spam))  # 重新入栈
        return spam


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

S = StockSpanner()
S.next(31)
S.next(41)
S.next(48)
S.next(59)
S.next(79)
