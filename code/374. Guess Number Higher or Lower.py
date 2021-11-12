#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :374. Guess Number Higher or Lower.py
# @Time      :11/12/21 12:25 AM
# @Author    :Eason Tang
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n + 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if guess(mid) > 0:
                lo = mid + 1
            elif guess(mid) < 0:
                hi = mid - 1
            else:
                return mid
