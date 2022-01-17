#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :539. Minimum Time Difference.py
# @Time      :1/17/22
# @Author    :Eason Tang
from typing import List, Optional


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minute(time: str):
            return int(time[:2]) * 60 + int(time[3:])

        timePoints.sort()
        ans = float('inf')
        # Some optimization to reduct convert time
        t0_minute = convert_to_minute(timePoints[0])
        pre_minute = t0_minute
        # End Some optimization to reduct convert time

        for i in range(1, len(timePoints)):
            cur_minute = convert_to_minute(timePoints[i])
            ans = min(ans, cur_minute - pre_minute)
            pre_minute = cur_minute

        ans = min(ans, convert_to_minute(timePoints[0]) + 1440 - convert_to_minute(timePoints[-1]))
        return ans
