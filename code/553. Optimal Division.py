#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :553. Optimal Division.py
# @Time      :2/26/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        """
        主要思想是使分母最小，因此用第一个数做分子，余下所有数相除后则可以使分母最小
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f'{nums[0]}/{nums[1]}'
        nums = [str(x) for x in nums]
        divider = '/'.join(nums[1:])
        return f'{nums[0]}/({divider})'
