# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1822. Sign of the Product of an Array.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:  # 任何数乘以0都是0
            return 0
        isPositive = True  # 乘积为正
        for num in nums:
            if num < 0:  # 每遇到一个负号
                isPositive = not isPositive  # 乘积反转
        return 1 if isPositive else -1
