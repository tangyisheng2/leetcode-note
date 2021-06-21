#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :139. Word Break.py
# @Time      :2021/6/21 12:15 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":  # basecase
            return True
        if s in self.memo:  # DP memorization
            return self.memo[s]

        for word in wordDict:
            if word in s and s.index(word) == 0:
                suffix = s.split(word, 1)[1]
                if self.wordBreak(suffix, wordDict):
                    self.memo[suffix] = True
                    return self.memo[suffix]

        self.memo[s] = False
        return self.memo[s]


test = Solution()
# ret = test.wordBreak(
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
#     ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
ret = test.wordBreak("aaaaaaa",
                     ["aaaa", "aaa"])
print(ret)
