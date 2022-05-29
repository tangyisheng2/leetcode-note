#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :853. Car Fleet.py
# @Time      :5/24/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                ans += 1  # if lead arrives sooner, it can't be caught
            else:
                times[-1] = lead  # else, fleet arrives at later time 'lead' (the slower one)

        return ans + bool(times)  # remaining car is fleet (if it exists)
