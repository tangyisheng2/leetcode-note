#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2100. Find Good Days to Rob the Bank.py
# @Time      :3/5/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """
        动态规划：left和right存储左边和右边连续非递增和连续非递减的数量
        """
        n = len(security)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                # 如果当天守卫比前一天守卫低，则最大天数 + 1，否则设为0（跳过）
                left[i] = left[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                right[n - i - 1] = right[n - i] + 1
        # 遍历日期返回震Good Rob Day
        return [i for i in range(time, n - time) if left[i] >= time and right[i] >= time]
