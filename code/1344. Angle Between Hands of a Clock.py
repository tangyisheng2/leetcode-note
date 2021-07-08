# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1344. Angle Between Hands of a Clock.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import math


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_mark_angle = 6
        hour_mark_angle = 30

        hour_angle = hour_mark_angle * (hour + minutes / 60)
        min_angle = min_mark_angle * minutes
        res = abs(hour_angle - min_angle)
        return res if res <= 180 else 360 - res