#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :934. Shortest Bridge.py
# @Time      :10/29/21 11:50 PM
# @Author    :Eason Tang
from typing import List


# class Solution:
#     def shortestBridge(self, grid: List[List[int]]) -> int:
#         """
#         1. 使用DFS找出其中一个岛屿（将这些岛屿标记为2），并将该岛屿的所有节点添加到BFS的队列中
#         2. BFS判断最短路径（2链接到1的最短路径）
#         """
#         m = len(grid)
#         n = len(grid[0])
#
#         def dfs(grid, x, y, q):
#             grid[x][y] = 2
#             q.append((x, y, 0))
#
#             for ne_x, ne_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
#                 if 0 <= ne_x < len(grid) and 0 <= ne_y < len(grid[0]) and grid[ne_x][ne_y] == 1:
#                     dfs(grid, ne_x, ne_y, q)
#
#         import collections
#         q = collections.deque()
#         flag = 0
#         for x in range(m):
#             for y in range(n):
#                 if grid[x][y] == 1:
#                     dfs(grid, x, y, q)
#                     flag = 1
#                     break
#             if flag:
#                 break
#
#         while q:
#             cur_x, cur_y, distance = q.popleft()
#             if grid[cur_x][cur_y] == 1:
#                 return distance - 1
#             grid[cur_x][cur_y] = 2
#
#             for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
#                 if 0 <= ne_x < m and 0 <= ne_y < n and grid[ne_x][ne_y] != 2:
#                     q.append((ne_x, ne_y, distance + 1))

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        1. 使用DFS找出其中一个岛屿（将这些岛屿标记为2），并将该岛屿的所有节点添加到BFS的队列中
        2. BFS判断最短路径（2链接到1的最短路径）
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, x, y, q):
            grid[x][y] = 2
            q.append((x, y, 0))

            for ne_x, ne_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= ne_x < len(grid) and 0 <= ne_y < len(grid[0]) and grid[ne_x][ne_y] == 1:
                    dfs(grid, ne_x, ne_y, q)

        import collections
        q = collections.deque()
        flag = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    dfs(grid, x, y, q)
                    flag = 1
                    break
            if flag:
                break

        while q:
            cur_x, cur_y, distance = q.popleft()

            for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
                if 0 <= ne_x < m and 0 <= ne_y < n and grid[ne_x][ne_y] != 2:
                    if grid[ne_x][ne_y] == 1:
                        return distance
                    grid[ne_x][ne_y] = 2    # 在这里染色，避免重复添加
                    q.append((ne_x, ne_y, distance + 1))


test = Solution()
# ret = test.shortestBridge([[1, 1, 1, 1, 1],
#                      [1, 0, 0, 0, 1],
#                      [1, 0, 1, 0, 1],
#                      [1, 0, 0, 0, 1],
#                      [1, 1, 1, 1, 1]])
ret = test.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])

print(ret)
