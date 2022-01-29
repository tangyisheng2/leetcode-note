#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :884. Uncommon Words from Two Sentences.py
# @Time      :1/29/22
# @Author    :Eason Tang
from typing import List, Optional
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        A word is uncommon if it
        1. appears exactly once in one of the sentences
        2. does not appear in the other sentence.
        which is equals to this statements:
        A word is uncommon if it appears only once in two string combined
        :param s1:
        :param s2:
        :return:
        """
        import collections
        s1_arr = s1.split(" ")
        s2_arr = s2.split(" ")

        hashmap = collections.Counter(s1_arr) + collections.Counter(s2_arr)

        ans = []
        for word, count in hashmap.items():
            if count == 1:
                ans.append(word)
        return ans