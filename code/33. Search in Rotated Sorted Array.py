#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :33. Search in Rotated Sorted Array.py
# @Time      :11/9/21 10:49 PM
# @Author    :Eason Tang
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                # 如果左半部分是有序的
                # 并且target在[l, mid]两个数的区间内，取左边区间
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # 否则取右边区间
                else:
                    l = mid + 1
            elif nums[l] >= nums[mid]:
                # 如果左半部分是无序的
                # 且target在[mid, r]这一个有序的区间内，取右边区间
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                # 否则取左边无序的区间
                else:
                    r = mid - 1

        return -1