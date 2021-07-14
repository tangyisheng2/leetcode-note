# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1647. Minimum Deletions to Make Character Frequencies Unique.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        """
        贪心
        :param s:
        :return:
        """
        ans = 0
        freq_set = set()
        character_freq = collections.Counter(s).values()

        for freq in character_freq:
            while freq in freq_set:
                freq -= 1
                ans += 1
            freq_set.add(freq)
        return ans


test = Solution
test.minDeletions(s="aabc")
