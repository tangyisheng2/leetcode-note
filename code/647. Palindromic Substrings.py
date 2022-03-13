# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   647. Palindromic Substrings.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         ans = 0
#         n = len(s)
#         for i in range(n):
#             ans += 1  # 本身单独一个字母是回文
#             # if i - 1 >= 0 and s[i] == s[i - 1]: # 判断前后一个字母是否可以组成两个字母的回文
#             #     ans += 1
#             # 判断前后一个字母是否可以组成两个字母的回文，这里只需要向后判断：此处向前判断与上一位向后判断会重复
#             if i + 1 < n and s[i] == s[i + 1]:
#                 ans += 1
#             lo = i - 1  # 开始判断3个字母以上的回文
#             hi = i + 1
#             while lo >= 0 and hi < n:
#                 if s[lo] == s[hi]:
#                     ans += 1
#                 lo -= 1
#                 hi += 1
#         return ans

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(0, 2 * n - 1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                ans += 1
        return ans

    def countSubstrings2(self, s: str) -> int:
        def count(idx):
            """
            This function counts the number of palindromic substrings center at idx
            """
            # The maximun palidrone sub-string length is odd
            l = idx
            r = idx
            ans = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            # The maximun palidrone sub-string length is even
            l = idx - 1
            r = idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            return ans

        return sum([count(idx) for idx in range(len(s))])


test = Solution()
test.countSubstrings("fdsklf")
