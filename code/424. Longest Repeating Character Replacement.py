#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :424. Longest Repeating Character Replacement.py
# @Time      :3/9/22
# @Author    :Eason Tang


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. Use 2 pointer to represent the sub-string
        2. Maximize the window, check if the window is valid:
        2.1 len(s) - max_occurance is our operation needed to modify the substring
        3. if valid, expand the window, else move the window right
        4. when the r pointer reaches the end, the window is the largest window
        """
        import collections
        ans = 0
        n = len(s)
        occurance = collections.defaultdict(int)

        l = 0
        r = 0
        max_occurance = 0

        while r < n:
            occurance[s[r]] += 1
            max_occurance = max(max_occurance, occurance[s[r]])  #

            if r - l + 1 - max_occurance > k:  # Window in not valid
                occurance[s[l]] -= 1  # Move the left pointer
                l += 1
            r += 1

        return r - l
