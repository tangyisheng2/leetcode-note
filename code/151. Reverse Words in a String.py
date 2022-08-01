#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :151. Reverse Words in a String.py
# @Time      :7/29/22
# @Author    :Eason Tang


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        双端队列
        """
        import collections
        l = 0
        r = len(s) - 1

        # Remove leading space
        while s[l] == ' ':
            l += 1
        # Remove the very last space
        while s[r] == ' ':
            r -= 1

        q, cur_word = collections.deque(), []

        while l <= r:
            if s[l] == ' ' and cur_word:
                q.appendleft("".join(cur_word))
                cur_word = []
            elif s[l] != ' ':
                cur_word.append(s[l])
            l += 1

        if cur_word:
            q.appendleft("".join(cur_word))

        return " ".join(q)
