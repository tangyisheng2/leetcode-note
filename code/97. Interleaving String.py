#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :97. Interleaving String.py
# @Time      :8/30/22
# @Author    :Eason Tang


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Use DP
        Sub-problem: s1[:i] and s2[:j] can from s3[:i + j - 1]
        DP matix: (i + 1) * (j + 1), default value is False
        Base Case:
        1. dp[0][0] = True
        2. Use s1 only to construct: For the first row: dp[i][0] = True if (dp[i - 1][0] == True and s1[i - 1] == s3[i - 1]
        3. Use s2 only to construct: For the first column: dp[0][j] = True if (dp[0][j - 1] == True and s2[j - 1] == s3[i - 1])
        Transistion Function:
        dp[i][j] == True if (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                        go from s1[:i - 1] + s2[:j] to make s3 s3[:i + j - 1] and add one more character from s1
                        or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                        go from s1[:i] + s2[:j - 1] to make s3 s3[:i + j - 1] and add one more character from s2
        """
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False
        # row = s1, col = s2
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]

        # Base Case 1
        dp[0][0] = True
        # Base Case 2
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        print(dp)
        return dp[-1][-1]


test = Solution()
print(test.isInterleave(s1="b", s2="cb", s3="cbb"))
