#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1342. Number of Steps to Reduce a Number to Zero.py
# @Time      :1/31/22
# @Author    :Eason Tang


class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num > 0:
            if num % 2:
                num -= 1
            else:
                num /= 2
            ans += 1
        return ans
