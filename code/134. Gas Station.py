#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :134. Gas Station.py
# @Time      :2021/7/2 5:00 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        :param gas:
        :param cost:
        :return:
        """
        station_cnt = len(gas)
        i = 0
        while i < station_cnt:
            oil = gas[i]  # initial oil we have
            for j in range(station_cnt):  # start travel
                """
                (i + j) % station_cnt means:
                we start from i,
                travel j station forward,
                then, since we travel in a loop,
                we use "%" to make sure that the index loops
                """
                oil -= cost[(i + j) % station_cnt]  # oil after travel
                if oil < 0:  # if our oil is below zero, we are not gonna make it
                    i = i + j
                    # 优化，见：https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-leetcode-solution/
                    break
                oil += gas[(i + j + 1) % station_cnt]  # refill oil in the next station
            if oil >= 0:  # if oil is greater than 0 after travel
                return i  # result found
            i += 1
        return -1  # else this travel is impossible


test = Solution()
# ret = test.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
ret = test.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3])
print(ret)
