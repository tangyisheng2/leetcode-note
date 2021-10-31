#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :37. Sudoku Solver.py
# @Time      :10/24/21 9:27 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def fill(board, x, y):
            # 以行优先进行填充
            if y == 9:
                return True  # 填充到行的最后一个元素，返回True

            nx = (x + 1) % 9
            ny = y + 1 if nx == 0 else y

            if board[y][x] != '.':
                return fill(board, nx, ny)

            for i in range(9):
                bx = x // 3
                by = y // 3
                box_key = by * 3 + bx
                if (not row[y][i]) and (not col[x][i]) and (not box[box_key][i]):
                    row[y][i] = True
                    col[x][i] = True
                    box[box_key][i] = True
                    board[y][x] = chr(i + ord('0'))
                    if fill(board, nx, ny):
                        return True
                    board[y][x] = '.'
                    row[y][i] = False
                    col[x][i] = False
                    box[box_key][i] = False
            return False

        row = [[False] * 10 for _ in range(9)]
        col = [[False] * 10 for _ in range(9)]
        box = [[False] * 10 for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                if ch != '.':
                    number = ord(ch) - ord('0')
                    bx, by = j // 3, i // 3
                    row[i][number] = True
                    row[j][number] = True
                    box[by * 3 + bx][number] = True

        fill(board, 0, 0)
        print(board)


test = Solution()
test.solveSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                 )
