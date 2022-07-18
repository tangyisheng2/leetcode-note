#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :289. Game of Life.py
# @Time      :7/17/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def calculate_live(x, y):
            ans = 0
            for nx, ny in [(x + 1, y),
                           (x - 1, y),
                           (x, y + 1),
                           (x, y - 1),
                           (x + 1, y + 1),
                           (x + 1, y - 1),
                           (x - 1, y + 1),
                           (x - 1, y - 1)]:
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    ans += board[nx][ny]
            return ans

        m = len(board)
        n = len(board[0])

        op = []

        for x in range(m):
            for y in range(n):
                live_cnt = calculate_live(x, y)
                if live_cnt == 2:
                    continue
                elif live_cnt == 3:
                    op.append((x, y, 1))
                else:
                    op.append((x, y, 0))

        for x, y, res in op:
            board[x][y] = res

        return None
