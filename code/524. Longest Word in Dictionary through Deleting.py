#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :524. Longest Word in Dictionary through Deleting.py
# @Time      :5/26/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """
        双指针做法
        :param s: 字符串
        :param dictionary: 单词列表
        :return:
        """
        dictionary.sort(key=lambda x: (-len(x), x))  # 按字符串长度降序排序，若相同则按字典序升序排序

        for word in dictionary:
            idx_word = 0
            idx_string = 0

            while idx_word < len(word) and idx_string < len(s):
                if word[idx_word] == s[idx_string]:
                    idx_word += 1
                idx_string += 1

                if idx_word == len(word):
                    return word
        return ""
