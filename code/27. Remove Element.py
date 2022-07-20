#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :27. Remove Element.py
# @Time      :7/19/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        使用快慢指针，当慢指针的元素与要移除的元素相等的时候使用快指针的元素覆盖
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        观察到judger中会对返回的数组进行排序，可知修改后数组的顺序不影响答案，因此我们可以直接把数组末尾数据放在需要移除数据的位置上，并且将数组大小变量 -1
        """
        left = 0
        length = len(nums)
        while left < length:
            if nums[left] == val:
                nums[left] = nums[length - 1]
                length -= 1

            else:
                left += 1

        return length