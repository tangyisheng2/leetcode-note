#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1020. Number of Enclaves.py
# @Time      :2/11/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        1. start dfs from border nodes, mark visted nodes to 0
        2. calculate the number of 1 in the grid
        """

        def dfs(x, y):
            """
            Traverse the graph, mark visted node to 0
            """
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return

            grid[x][y] = 0

            for (nx, ny) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                dfs(nx, ny)

        ans = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 1:
                    dfs(i, j)
        # All lands that are not Enclaves are marked to 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += 1

        return ans
