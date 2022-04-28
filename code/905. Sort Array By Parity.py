#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :905. Sort Array By Parity.py
# @Time      :4/27/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
