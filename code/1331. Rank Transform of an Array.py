#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1331. Rank Transform of an Array.py
# @Time      :7/27/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]
