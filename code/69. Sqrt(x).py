#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :69. Sqrt(x).py
# @Time      :11/9/21 10:36 PM
# @Author    :Eason Tang
class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x

        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid > x:
                hi = mid - 1
            else:
                lo = mid + 1

        return hi   # 在此处求小于x的第一个整数，因此选择hi

test = Solution()
test.mySqrt(4)