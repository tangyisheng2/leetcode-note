#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1403. Minimum Subsequence in Non-Increasing Order.py
# @Time      :8/3/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort()
        sum_prefix = [0] * len(nums)
        # Build prefix sum
        for i in range(len(nums)):
            if i == 0:
                sum_prefix[0] = nums[0]
            else:
                sum_prefix[i] = sum_prefix[i - 1] + nums[i]

        # Iterate through the prefix sum in reverse order
        for i in range(len(sum_prefix) - 1, -1, -1):
            sub_seq = sum_prefix[-1] - sum_prefix[i]
            remainder = sum_prefix[i]
            if sub_seq > remainder:
                return sorted(nums[i + 1:], reverse=True)
        return nums  # the base case is to return the whole seq (the sum of a non-empty seq is always bigger than an
        # empty seq)
