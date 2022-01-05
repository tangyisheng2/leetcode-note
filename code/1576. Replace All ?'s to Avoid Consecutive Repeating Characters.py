#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1576. Replace All ?'s to Avoid Consecutive Repeating Characters.py
# @Time      :1/5/22 12:50 AM
# @Author    :Eason Tang
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                for ch in 'abc':  # To avoid consecutive, we just need to iterate through 'abc'
                    if ch != s[max(0, i - 1)] and ch != s[min(len(s) - 1, i + 1)]:  # We need to avoid index error
                        s[i] = ch
                        break

        return ''.join(s)
