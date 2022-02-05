#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1219. Path with Maximum Gold.py
# @Time      :2/4/22
# @Author    :Eason Tang
from typing import List, Optional


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(cur_x, cur_y, cur_gold):
            """
            This function traverse the map and update the maximum gold
            不实用Global Visited的原因：
            1. 数据量相对较少
            2. 使用global_visited时会漏掉可能存在的点
            eg. 6 -> 8 -> 9 = 23后就结束
            然而实际上应该为7 -> 8 -> 9
            在第一次访问总7会被添加到global_visited但是6 -> 8 -> 7并不是最大，因此错过
            """
            nonlocal ans
            if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m or not grid[cur_x][cur_y]:
                return

            cur_gold += grid[cur_x][cur_y]

            ans = max(ans, cur_gold)
            # global_visited.add((cur_x, cur_y))
            og_num = grid[cur_x][cur_y]
            grid[cur_x][cur_y] = 0
            for (ne_x, ne_y) in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
                dfs(ne_x, ne_y, cur_gold)
            grid[cur_x][cur_y] = og_num

        n, m = len(grid), len(grid[0])
        ans = 0
        # global_visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i, j):
                    dfs(i, j, 0)
        return ans


test = Solution()
ret = test.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]])
