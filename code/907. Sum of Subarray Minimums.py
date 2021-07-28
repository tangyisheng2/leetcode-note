# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   907. Sum of Subarray Minimums.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0

        arr = [-1] + arr + [-1]
        stack = []

        for i, a in enumerate(arr):
            while stack and arr[stack[-1]] > a:
                cur = stack.pop()
                res += arr[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return int(res % (1e9 + 7))


if __name__ == '__main__':
    ret = Solution().sumSubarrayMins(arr=[3, 1, 2, 4])
