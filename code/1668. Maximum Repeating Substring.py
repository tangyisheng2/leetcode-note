#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1668. Maximum Repeating Substring.py
# @Time      :9/30/21 12:15 AM
# @Author    :Eason Tang

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        n = len(sequence)
        m = len(word)
        seq_ptr = 0
        for i in range(n - m + 1):
            index = 0
            count = 0
            for j in range(i, n):
                if sequence[j] == word[index]:
                    index = (index + 1) % m
                    count += 1
                else:
                    break
            ans = max(ans, count / m)
        return ans


print(Solution().maxRepeating(sequence="ababc", word="ab"))
