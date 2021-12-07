#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1034. Coloring A Border.py
# @Time      :12/7/21 11:03 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def check_boundary(grid, x, y):
            """
            Return if grid[x][y] is a boundary element
            :param grid:
            :param x:
            :param y:
            :return:
            """
            if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
                return True
            elif grid[x][y] != grid[x + 1][y] or grid[x][y] != grid[x - 1][y] or grid[x][y] != grid[x][y + 1] or \
                    grid[x][y] != grid[x][y - 1]:
                return True
            return False

        def dfs(grid, x, y, visited, og_color, color, boarder_element):
            """
            Traverse through all the component and return border elment
            """
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in visited or grid[x][y] != og_color:
                return
            else:
                visited.add((x, y))

            if check_boundary(grid, x, y):
                boarder_element.add((x, y))

            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in dir:
                ne_x, ne_y = x + dx, y + dy

                dfs(grid, ne_x, ne_y, visited, og_color, color, boarder_element)

        boarder_element = set()
        dfs(grid, row, col, set(), grid[row][col], color, boarder_element)
        print(boarder_element)
        for x, y in boarder_element:
            grid[x][y] = color

        return grid

test = Solution()
ret = test.colorBorder(
    [[1, 2, 1, 2, 1, 2], [2, 2, 2, 2, 1, 2], [1, 2, 2, 2, 1, 2]], 1, 3, 1)
