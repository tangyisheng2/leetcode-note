#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2055. Plates Between Candles.py
# @Time      :3/7/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        left = [-1] * n  # lcandle[i] 表示在位置 i 左侧(包括 i )，离 i 最近的蜡烛的位置
        right = [-1] * n  # rcandle[i] 表示在位置 i 右侧(包括 i )，离 i 最近的蜡烛的位置
        prefix_plate = [0] * n  # prefix_plate[i] 表示在位置 i 之前（左侧）的盘子个数
        ans = []

        if s[0] == '|':
            left[0] = 0

        if s[-1] == '|':
            right[-1] = n - 1

        for i in range(1, n):
            if s[i] == '|':
                left[i] = i
                prefix_plate[i] = prefix_plate[i - 1]
            else:
                left[i] = left[i - 1]
                prefix_plate[i] = prefix_plate[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if s[i] == '|':
                right[i] = i
            else:
                right[i] = right[i + 1]

        for start, end in queries:
            left_idx = right[start]
            right_idx = left[end]

            if left_idx >= 0 and right_idx >= 0 and left_idx < right_idx:
                ans.append(prefix_plate[right_idx] - prefix_plate[left_idx])
            else:
                ans.append(0)

        return ans
