#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :42. Trapping Rain Water.py
# @Time      :4/29/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        动态规划，在下标为i的点的垂直方向集雨量为：
        min(左边的第一个高度最大值，右边的第一个高度最大值) - height[i]

        暴力解法：对于每一个点，向左向右扫描最大值
        DP预处理：
        先从左向右扫描一遍height，对每一个height[i]记录左边高度最大值
        再从右向左扫描一边height，对每一个height[i]记录右边高度最大值
        """
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans
