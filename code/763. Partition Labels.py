# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   763. Partition Labels.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        贪心算法
        先求出第一个字母最后出现的idx，保证第一个字幕全部被分到第一区间
        紧接着遍历第一区间内的字母，并根据每一个字幕最后出现的位置扩大上界，以保证这些字母都在我们的区间内
        最后就得最后的分区
        :param s:
        :return:
        """
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition
