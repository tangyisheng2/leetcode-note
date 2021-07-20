# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   453. Minimum Moves to Equal Array Elements.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        给玩数学的跪了
        https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/solution/python3-yi-xing-dai-ma-ji-bai-99-diao-ch-25ar/
        :param nums:
        :return:
        """
        return sum(nums) - min(nums) * len(nums) if len(set(nums)) > 1 else 0
