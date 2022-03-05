#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :49. Group Anagrams.py
# @Time      :3/4/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        对str中字母进行字典序排序
        :param strs:
        :return:
        """
        import collections
        hashmap = collections.defaultdict(list)

        for word in strs:
            hashmap[''.join(sorted(word))].append(word)

        return [[x for x in word] for word in hashmap.values()]

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        import collections
        hashmap = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            hashmap[tuple(count)].append(word)

        return [anagran for anagran in hashmap.values()]
