#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :81. Search in Rotated Sorted Array II.py
# @Time      :11/9/21 11:58 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            """
            对于数组中有重复元素的情况，二分查找时会出现a[l] == a[mid] == a[r]，此时无法判断区间[l, mid]和[mid + 1, r]哪个是有序的
            例如nums = [3, 1, 2, 3, 3], target = 2，首次二分时无法判断区间[0, 3]和区间[4, 6]哪个是有序的
            对于这种情况，我们只能将当前二分区间的左边界加一，右边界减一，然后在新区间上继续二分查找。
            """
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1

            # Have 2 cases here:
            # 1. if [l, mid] is sorted
            elif nums[l] <= nums[mid]:
                # and if target is in [l, mid], we shrink the range to [l, mid - 1]
                # else we shrink the range to [mid + 1, r]
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 2. if [mid, r] is sorted
            else:
                # if target is in [mid, r], shrink the range to [mid + 1, r]
                # else shrink the range to [l, mid - 1]
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
