#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1688. Count of Matches in Tournament.py
# @Time      :1/24/22
# @Author    :Eason Tang

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
                ans += n
            elif n % 2:
                ans += (n - 1) // 2 + 1
                n = (n - 1) // 2
        return int(ans)
