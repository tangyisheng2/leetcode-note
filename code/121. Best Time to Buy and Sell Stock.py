#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :121. Best Time to Buy and Sell Stock.py
# @Time      :3/1/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        单调栈
        :param prices:
        :return:
        """
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:  # 无法完成买入卖出动作
            return 0

        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0  # 下标i天结束的时候卖出股票，手上持有的现金数
        dp[0][1] = -prices[0]  # 下标为i天结束的时候，持有股票，手上持有的现金数

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 第i天结束不持有股票（当天卖出），最大利润为：前一天不持有股票的现金数 或 前一天持有股票今天以price[i]卖出后的现金数
            dp[i][1] = max(dp[i - 1][1], -prices[i])
            # 第i天结束时持有股票，当天的现金数为：前一天持有股票的现金数 或 当天买入后余下的现金数

        return dp[-1][0]  # 因为在最后一天我们必须卖出股票，因此返回不持有股票的数值
