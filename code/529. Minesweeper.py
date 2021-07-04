#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :529. Minesweeper.py
# @Time      :2021/7/4 10:51 PM
# @Author    :Eason Tang

from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def neighbours(x, y):
            """
            周围节点的generator，用来生成周围节点
            同时判断是否越界
            :param x:
            :param y:
            :return:
            """
            ne_dir = [(x + 1, y), (x - 1, y),
                      (x, y + 1), (x, y - 1),
                      (x + 1, y + 1), (x - 1, y + 1),
                      (x + 1, y - 1), (x - 1, y - 1)]
            for ne_x, ne_y in ne_dir:
                if 0 <= ne_x < len(board) and 0 <= ne_y < len(board[0]):
                    yield ne_x, ne_y

        def count_mine(x, y):
            """
            计算该节点周围的地雷数量
            :param x:
            :param y:
            :return:
            """
            mine_count = 0
            for ne_x, ne_y in neighbours(x, y):
                if board[ne_x][ne_y] == "M":
                    mine_count += 1
            return mine_count

        def dfs(x, y):
            """
            从节点开始进行遍历
            :param x:
            :param y:
            :return:
            """
            if board[x][y] != "E":  # 如果节点已经遍历过
                return  # 返回
            mine_count = count_mine(x, y)
            if mine_count:  # 检查节点附近是否有Mine
                board[x][y] = str(mine_count)  # 如果有则填入Mine的数量
                return  # 因为遇到了Mine所以就要返回
            else:
                board[x][y] = "B"  # 没有Mine，填入Blank
            for ne_x, ne_y in neighbours(x, y):
                dfs(ne_x, ne_y)  # 继续遍历相邻的节点

        def update(x, y):
            """
            检测节点类型，更新表格
            :param x:
            :param y:
            :return:
            """
            if board[x][y] == "M":  # 如果Mine炸了
                board[x][y] = "X"  # 更新表格
                return board  # 结束游戏
            else:
                dfs(x, y)  # 否则开始遍历
                return board

        update(click[0], click[1])
        return board


test = Solution()
ret = test.updateBoard([['E', 'E', 'E', 'E', 'E'],
                        ['E', 'E', 'M', 'E', 'E'],
                        ['E', 'E', 'E', 'E', 'E'],
                        ['E', 'E', 'E', 'E', 'E']],
                       [3, 0])
print(ret)
