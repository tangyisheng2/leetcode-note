#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :883. Projection Area of 3D Shapes.py
# @Time      :4/25/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        """
        模拟法
        grid = [[1,2],[3,4]]
        grid[0][0]放置一层高v = 1
        grid[0][1]放置两层高v = 2
        如此类推
        :param grid:
        :return:
        """
        # xy = sum(v > 0 for row in grid for v in row)
        # xz = sum(map(max, zip(*grid)))
        # yz = sum(map(max,grid))

        n = len(grid)
        ans = 0

        for i in range(n):
            xz = 0
            yz = 0
            for j in range(n):
                ans += 1 if grid[i][j] > 0 else 0
                yz = max(yz, grid[i][j])  # 获取grid中每一行的最大值（用于在yz投影相加）
                xz = max(xz, grid[j][i])  # 获取grid中每一列的最大值（用于在xz投影中相加）
            ans += yz + xz

        return ans
