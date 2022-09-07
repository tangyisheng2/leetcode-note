#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :122. Best Time to Buy and Sell Stock II.py
# @Time      :9/6/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Max Profit: Buy low sell high for as many times as we can
        Find every local minimun and local maximun, and add maximun - minimun to our answer,
        To find the local maximun number to the right of a number, we can use monolitic stack
        (from big to small)
        """

        stk = []
        ans = 0
        for num in prices:
            # 出现拐点，进行交易
            if stk and num > stk[-1]:
                ans += num - stk[-1]
            # 维护单调栈的单调递减性质
            while stk and num > stk[-1]:
                stk.pop()
            stk.append(num)
        return ans


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Use greedy, we just buy the stock and sell it tomorrow instead of keeping it for multiple days when the stock price is increasing
        e.g. [1,2,3,4,5]
        2ways to trade:
        1way is buy on day1, sell on day5, earn 4 units of profile
        2way is to buy on day1, sell on day2, earn 1 unit of profit, then buy it back immediately, and sell on day 3, loop this process, we will earn 1 unit/transaction, 4 transactions in total, the total profit is still 4
        """

        ans = 0
        for i in range(len(prices)):
            if i > 0:
                profit = max(0, prices[i] - prices[i - 1])  # Either not buy or buy it and sell tomorrow
                ans += profit
        return ans


test = Solution()
ret = test.maxProfit([7, 1, 5, 3, 6, 4])
print(ret)
