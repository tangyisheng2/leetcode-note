#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :908. Smallest Range I.py
# @Time      :4/29/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
