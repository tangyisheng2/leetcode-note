#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1011. Capacity To Ship Packages Within D Days.py
# @Time      :11/9/21 9:59 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_load(weights, max_weigh, max_day):
            if max(weights) > max_weigh:
                return False
            cur_weight = 0
            cur_day = 1
            for weight in weights:
                if cur_weight + weight > max_weigh:
                    cur_day += 1
                    cur_weight = weight

                else:
                    cur_weight += weight
            return cur_day <= max_day

        # print(can_load(weights, 11, days))
        lo = 0
        hi = sum(weights)

        while lo <= hi:
            mid = (lo + hi) // 2
            if can_load(weights, mid, days):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
