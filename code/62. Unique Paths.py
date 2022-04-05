#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :62. Unique Paths.py
# @Time      :4/4/22
# @Author    :Eason Tang
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Use dp:
        Corner Case: The left and upper bound to be all 1
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:  # Corner Case
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
