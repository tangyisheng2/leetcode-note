#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1984. Minimum Difference Between Highest and Lowest of K Scores.py
# @Time      :2/10/22
# @Author    :Eason Tang
from typing import List, Optional


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        1. sort the array
        2. create the sliding window contains k element, and the difference between the highest and the lowest in the window would be the last element minus the first
        3. slide the window and  update the ans
        """

        nums.sort()  # SORT ARRAY
        print(nums)
        ans = nums[-1] - nums[0]

        for ptr_r in range(k - 1, len(nums)):
            ptr_l = ptr_r - k + 1  # calculate ptr_l
            diff = nums[ptr_r] - nums[ptr_l]  # difference between the highest and the lowest

            ans = min(ans, diff)  # update ans

        return ans
