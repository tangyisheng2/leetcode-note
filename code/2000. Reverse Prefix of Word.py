#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2000. Reverse Prefix of Word.py
# @Time      :2/1/22
# @Author    :Eason Tang


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        return "".join(reversed(word[:idx + 1])) + word[idx + 1:]
