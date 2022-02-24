#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :827. Making A Large Island.py
# @Time      :2/23/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y, id):
            """
            This function adds all consecutive land to a set
            """
            nonlocal max_area
            if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited or grid[x][y] != 1:
                return

            visited.add((x, y))

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                dfs(nx, ny, id)  # Pay attention to recursive call

        def fill(x, y):
            """
            This function fills the land and returns the area after fill
            """
            ans = 1
            joint_island_id = set()
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 0 and grid[nx][ny][0] not in joint_island_id:
                    # print(grid[nx][ny], joint_island_id)
                    joint_island_id.add(grid[nx][ny][0])
                    ans += grid[nx][ny][1]

            return ans

        n = len(grid)
        m = len(grid[0])
        ans = 0
        island_id = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited = set()
                    dfs(i, j, 0)
                    island_id += 1
                    max_area = len(visited)  # Count the maximun area
                    for (x, y) in visited:
                        grid[x][y] = (island_id, max_area)
                    ans = max(ans, max_area)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    ans = max(ans, fill(i, j))

        return ans


test = Solution()
test.largestIsland([[1, 0], [0, 1]])
