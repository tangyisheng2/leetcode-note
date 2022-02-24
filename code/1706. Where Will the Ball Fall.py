#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1706. Where Will the Ball Fall.py
# @Time      :2/23/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def fall(ball_column):
            """
            This function calculate the fall point of the ball
            1. right and right: goes right [x + 1, y + 1]
            2. left and left: goes left [x - 1, y + 1]
            3. right and left: stops -> return -1
            """
            RIGHT = 1
            LEFT = -1
            row = 0
            col = ball_column
            while row < n:
                if grid[row][col] == RIGHT and col + 1 < m and grid[row][col + 1] == RIGHT:
                    row, col = row + 1, col + 1
                    print(row, col, 'right')
                elif grid[row][col] == LEFT and col - 1 >= 0 and grid[row][col - 1] == LEFT:
                    row, col = row + 1, col - 1
                    print(row, col, 'left')
                else:
                    print(row, col, 'oops')
                    return -1
            return col

        n = len(grid)
        m = len(grid[0])
        return [fall(x) for x in range(m)]


test = Solution()
test.findBall(grid=[[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]])
