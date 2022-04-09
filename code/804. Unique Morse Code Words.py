#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :804. Unique Morse Code Words.py
# @Time      :4/9/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = set()

        def getMorseCode(ch):
            morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                     "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                     "--.."]
            return morse[ord(ch) - ord('a')]

        for word in words:
            code = [getMorseCode(ch) for ch in word]
            ans.add(''.join(code))

        return len(ans)
