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


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int):
            """
            按行遍历数独
            """
            nonlocal valid
            if pos == len(spaces):  # 如果速度遍历完成（遍历到最后一行的下一行），则数独有解
                valid = True
                return

            i, j = spaces[pos]  # 每一行的第一个空格开始便利
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][
                    digit] == False:  # 如果在每一行，每一列，每一个九宫格中均没有占用
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True  # 更新占用情况
                    board[i][j] = str(digit + 1)  # 更新数独元素
                    dfs(pos + 1)  # 更新spaces数组中的下一个元素
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False  # backtracking回溯
                if valid:  # 如果数独合法，early stop
                    return

        line = [[False] * 9 for _ in range(9)]  # 一维：每一行的行坐标；二维：每一行中数字i（下标为i - 1）是否出现
        column = [[False] * 9 for _ in range(9)]  # 一维：每一行的行坐标；二维：每一列中数字i（下标为i - 1）是否出现
        block = [[[False] * 9 for _a in range(3)] for _b in
                 range(3)]  # 一维：每一个九宫格的坐标（从左到右从上到下）；二维：每一九宫格中数字i（下标为i - 1）是否出现
        valid = False  # 数独已经有解
        spaces = list()  # 空格位置

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))  # 遇到空格将其添加进spaces数组中，用于遍历
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True  # 否则将数字添加到used数组中

        dfs(0)


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
