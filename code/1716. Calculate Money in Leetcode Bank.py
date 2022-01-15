#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1716. Calculate Money in Leetcode Bank.py
# @Time      :1/15/22
# @Author    :Eason Tang
from typing import List, Optional


class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        day = n % 7
        """
        存满一周的base: week * 28
        从第二周开始每周的差额: 7 * (1 + week - 1) * (week - 1) // 2
        不满整周的天数: week * day
        不满整周的天数的差额: (1 + day) * day // 2
        """
        return week * 28 + 7 * (1 + week - 1) * (week - 1) // 2 + week * day + (1 + day) * day // 2


test = Solution()
test.totalMoney(20)
