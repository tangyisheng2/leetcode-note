# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   977. Squares of a Sorted Array.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums[i] *= nums[i]

        return sorted(nums)
