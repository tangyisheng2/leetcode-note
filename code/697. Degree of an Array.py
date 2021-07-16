# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   697. Degree of an Array.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        使用哈希表存储该数字的度，最早出现的idx和最晚出现的idx
        然后遍历哈希表并找到最短的数组
        更新结果的两个条件：
        1. degree比当前的最大值要大
        2. degree同当前的度相同，但是数组的长度要小于当前的结果
        :param nums:
        :return:
        """
        n = len(nums)
        freq = {}
        for i in range(n):  # Calculate degree
            if nums[i] not in freq:
                freq[nums[i]] = [0, i, i]
            freq[nums[i]][0] += 1  # 更新数组的度
            freq[nums[i]][2] = i  # 更新数字最后出现的位置

        max_degree = 0
        degree_len = n
        for num_degree, start, end in freq.values():
            if num_degree > max_degree or (num_degree == max_degree and end - start <= degree_len):
                max_degree = num_degree
                degree_len = end - start + 1

        return degree_len


test = Solution()
test.findShortestSubArray([1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2])
