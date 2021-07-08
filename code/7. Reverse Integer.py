# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   7. Reverse Integer.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def reverse(self, x: int) -> int:
        isPositive = 1 if x >= 0 else 0
        x = abs(x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        if abs(res) >= 2147483647:
            # If reversing x causes the value to go outside
            # the signed 32-bit integer range [-231, 231 - 1], then return 0.
            return 0
        return res if isPositive else -res
