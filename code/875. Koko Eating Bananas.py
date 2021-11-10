#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :875. Koko Eating Bananas.py
# @Time      :11/9/21 9:27 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k: int, h: int, piles: List[int]) -> bool:
            from math import ceil
            return sum(ceil(banana_count / k) for banana_count in piles) <= h

        lo = 1
        hi = max(piles)

        while lo <= hi:
            mid = (lo + hi) // 2
            if can_eat_all(mid, h, piles):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo   # 如果是求下界则返回


test = Solution()
test.minEatingSpeed(piles=[3, 6, 7, 11], h=8)
