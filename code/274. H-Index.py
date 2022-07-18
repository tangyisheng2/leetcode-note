#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :274. H-Index.py
# @Time      :7/17/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Sort the citations, iterate through the list from high to low
        h index starts at 0
        Given h index, if we found a citation that citations[i] > h, that means we have find a citation that have at least n+1 citation
        """
        # Sort citations
        citations.sort(reverse=True)
        i = 0
        h = 0
        while i < len(citations) and citations[i] > h:
            # 如果当前 H 指数为 h 并且在遍历过程中找到当前值 citations[i] > h，则说明我们找到了一篇被引用了至少 h+1 次的论文，所以将现有的 h 值加 1。
            i += 1
            h += 1

        return h
