#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1048. Longest String Chain.py
# @Time      :2021/6/23 8:35 PM
# @Author    :Eason Tang
# https://leetcode-cn.com/problems/longest-string-chain/solution/an-zhao-zi-fu-chuan-chang-du-pai-xu-hou-zai-yong-z/
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda words: len(words))
        dp = [1 for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(i):
                if self.isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def isPredecessor(self, word_pre, word):
        if len(word_pre) != len(word) - 1:
            return False
        i = 0
        j = 0
        while i < len(word_pre) and j < len(word):
            if word_pre[i] == word[j]:
                i += 1
                j += 1
            else:
                j += 1
                if j - 1 > 1:
                    return False
        if j >= len(word) - 1:
            return True
        return False


test = Solution()
ret = test.isPredecessor("abcd", "dbqca")
ret = test.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])
print(ret)
