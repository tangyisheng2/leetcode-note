# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   503. Next Greater Element II.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        联动#496
        使用取模操作实现循环数组
        :param nums:
        :return:
        """
        n = len(nums)
        stack = []
        hashmap = {}
        res = [-1] * len(nums)
        for i in range(2 * n):
            while stack and stack[-1][1] < nums[i % n]:
                pre_i, _ = stack.pop()
                hashmap[pre_i] = (i, nums[i % n])
            stack.append((i, nums[i % n]))

        for i in range(n):
            if i in hashmap:
                res[i] = hashmap[i][1]

        return res


if __name__ == '__main__':
    ret = Solution().nextGreaterElements(nums=[1, 2, 1])
