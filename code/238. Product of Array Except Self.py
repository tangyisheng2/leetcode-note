#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :238. Product of Array Except Self.py
# @Time      :2021/9/10 5:29 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_product = [0] * n  # 前缀乘积
        suffix_product = [0] * n  # 后缀乘积
        ans = [0] * n  # 结果

        prefix_product[0] = 1  # 因为两侧没有元素，所以他们的乘积是1
        suffix_product[n - 1] = 1

        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
            """
            nums:   [1, 2, 3, 4]
            prefix: [1, 0, 0 ,0]
            prefix[2] = prefix_product[1] * nums[1] 这样就是把自身除外的前缀和
            """

        for i in reversed(range(n - 1)):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = prefix_product[i] * suffix_product[i]

        return ans
