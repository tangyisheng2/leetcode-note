#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :26. Remove Duplicates from Sorted Array.py
# @Time      :7/17/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        use slow-fast pointer to  move the number forward
        """
        slow = 1
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                """
                Should not use nums[fast] != nums[fast - 1]:
                In example of [0,0,1,1,1,2,2,3,3,4]
                When it runs to slow = 3 and fast = 6; nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
                Since nums[3] != nums[6], thus nums = nums = [0, 1, 2, 2, 1, 2, 2, 3, 3, 4], which is not correct
                """
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


test = Solution()
test.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
