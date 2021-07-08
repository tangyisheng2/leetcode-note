# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   392. Is Subsequence.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if s == "":
            # 0 <= s.length <= 100
            # 0 <= t.length <= 104
            # 注意s, t为空的情况
            return True
        while j < len(t):
            if s[i] == t[j]:
                i += 1
            if i == len(s): # 如果在最后一个idx也相等的话，+=1后就会和s的长度相等了
                return True
            j += 1
        return False
