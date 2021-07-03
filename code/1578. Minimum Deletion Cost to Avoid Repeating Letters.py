#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1578. Minimum Deletion Cost to Avoid Repeating Letters.py
# @Time      :2021/7/3 2:12 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        """
        贪心算法：
        对于所有连续相同的元素，我们将其中删除cost最大的一个元素留下，并且删除其他的元素
        :param s:
        :param cost:
        :return:
        """
        ret = 0
        i = 0
        while i < len(s):
            ch = s[i]  # 需要比较的字符
            max_delete_cost = 0  # 记录最大的删除成本
            total_cost = 0  # 记录删除这一组连续字符的总成本
            while i < len(s) and s[i] == ch:
                # 由于初始条件下ch = s[i]，此循环一定会进入一次，用于移动指针
                total_cost += cost[i]  # 记录进总删除成本
                max_delete_cost = max(max_delete_cost, cost[i])  # 更新最大删除成本
                i += 1  # 指针右移
            ret += total_cost - max_delete_cost  # 保留删除cost最大的一个元素
        return ret


test = Solution()
test.minCost(s="abc", cost=[1, 2, 3])
