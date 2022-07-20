#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :187. Repeated DNA Sequences.py
# @Time      :7/18/22
# @Author    :Eason Tang
from typing import List

L = 10


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        import collections
        ans = []
        cnt = collections.defaultdict(int)
        for i in range(len(s) - L + 1):
            sub = s[i: i + L]
            cnt[sub] += 1
            if cnt[sub] == 2:
                # 只有在个数为2的时候添加到ans，防止重复
                ans.append(sub)
        return ans


bins = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        import collections
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:  # 进队9位作为预备
            x = (x << 2) | bins[ch]
        cnt = collections.defaultdict(int)
        for i in range(n - L + 1):
            x = ((x << 2) | bins[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            """
            1. x << 2: x左移两位，左移后最低两位为00
            2. bin[s[i + L - 1]] -> x = x | bin[ch]: 设置最低两位
            3. (1 << (L * 2)) - 1: 因为我们只要后20位，因此将左移后吐出来的两位归零
            """
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i: i + L])
        return ans


test = Solution2().findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
