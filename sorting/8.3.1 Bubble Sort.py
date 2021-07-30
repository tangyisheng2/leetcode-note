# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   8.3.1 Bubble Sort.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def bubble_sort(self, nums):
        for i in reversed(range(1, len(nums))):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


if __name__ == '__main__':
    ret = Solution().insertion_sort([2, 3, 1, 5])
    print(ret)
