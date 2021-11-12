#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :375. Guess Number Higher or Lower II.py
# @Time      :11/12/21 12:20 AM
# @Author    :Eason Tang
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}

        def dfs(l, r):
            if l >= r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            ans = float('inf')
            for i in range(l, r + 1):
                cur = max(dfs(l, i - 1), dfs(i + 1, r)) + i
                ans = min(ans, cur)

            memo[(l, r)] = ans
            return ans

        return dfs(1, n)