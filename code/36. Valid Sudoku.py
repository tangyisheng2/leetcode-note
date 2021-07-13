# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   36. Valid Sudoku.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[0] * 10 for _ in range(9)]  # 一维：每一行行号；二维：每个数字的出现次数（下标对应数字）
        col = [[0] * 10 for _ in range(9)]  # 一维：每一列列号；二维：每个数字的出现次数（下标对应数字）
        box = [[0] * 10 for _ in range(9)]  # 一维：每一个小box的编号，从左上到右下；二维：每个数字的出现次数（下标对应数字）
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                curNum = ord(board[i][j]) - ord('0')  # 获取目前方格的数字
                if row[i][curNum] != 0 or col[j][curNum] != 0 or box[j // 3 + (i // 3) * 3][curNum] != 0:
                    # 1. 当前行当前数字的出现次数大于1，返回否
                    # 2. 当前列当前数字的出现次数大于1，返回否
                    # 3. 3 x 3的小范围的出现次数大于1，返回否
                    return False
                row[i][curNum], col[j][curNum], box[j // 3 + (i // 3) * 3][curNum] = 1, 1, 1  # 更新三个2D数组
        return True
