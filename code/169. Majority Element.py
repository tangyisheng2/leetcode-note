#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :169. Majority Element.py
# @Time      :2021/8/26 6:01 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import collections
        counter = collections.Counter(nums)
        max_val = max(counter.values())
        for key, val in counter.items():
            if val == max_val:
                return key


if __name__ == '__main__':
    ret = Solution().majorityElement([2, 3, 2])
