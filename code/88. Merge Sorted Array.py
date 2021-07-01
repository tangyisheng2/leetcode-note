#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :88. Merge Sorted Array.py
# @Time      :2021/6/28 12:48 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


test = Solution()
test.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
