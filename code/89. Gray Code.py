#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :89. Gray Code.py
# @Time      :1/8/22 11:01 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        # https://leetcode-cn.com/problems/gray-code/solution/ge-lei-bian-ma-by-leetcode-solution-cqi7/1321067
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

test = Solution()
test.grayCode(2)