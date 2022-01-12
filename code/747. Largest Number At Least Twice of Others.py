#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :747. Largest Number At Least Twice of Others.py
# @Time      :1/12/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_1st = (-1, -1)
        max_2nd = (-1, -1)

        for index, val in enumerate(nums):
            if val > max_1st[0]:    # If found a new maximum
                max_2nd = max_1st
                max_1st = (val, index)
            elif val > max_2nd[0]:  # If found a new 2nd maximum
                max_2nd = (val, index)

        return max_1st[1] if (max_1st[0] >= 2 * max_2nd[0]) else -1
