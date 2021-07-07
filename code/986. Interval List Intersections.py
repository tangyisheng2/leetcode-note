# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   986. Interval List Intersections.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import collections
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])  # 起始点在first和second起始点的最大值
            hi = min(firstList[i][1], secondList[j][1])  # 结束点在first和second末端点的最小值
            if lo <= hi:  # 确认是否真的相交
                ans.append([lo, hi])
            # 如果 B 中存在两个区间均与 A[0] 相交，那么它们将共同包含 A[0] 的末端点，但是 B 中的区间应该是不相交的，所以存在矛盾。
            if firstList[i][1] < secondList[j][1]:  # 对于提前结束的区间，我们考察他的下一个区间
                i += 1
            else:
                j += 1

        return ans
