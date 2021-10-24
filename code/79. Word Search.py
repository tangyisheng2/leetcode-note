#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :79. Word Search.py
# @Time      :2021/6/23 9:17 PM
# @Author    :Eason Tang
import collections
from typing import List

"""
[["C","A","A"],["A","A","A"],["B","C","D"]]
"AAB"
在BFS时候，可能会出现board和word都有多次重复的情况，在这个时候BFS比较难处理这种问题
"""


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         """
#         BFS
#         :param board: an m x n grid of characters board
#         :param word: a string word
#         :return: return true if word exists in the grid
#         """
#
#         def neighbours(cur_x, cur_y):
#             for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
#                 if 0 <= ne_x < m and 0 <= ne_y < n and \
#                         (ne_x, ne_y) not in visited and \
#                         next_ch_idx < len(word) and \
#                         board[ne_x][ne_y] == word[next_ch_idx]:
#                     yield ne_x, ne_y
#
#         queue = collections.deque()
#         visited = set()
#
#         m = len(board)
#         n = len(board[0])
#
#         next_ch_idx = 1  # 首字母的下一个字母（我们第一次要搜寻这个）
#
#         for x in range(m):  # 找到开头字母
#             for y in range(n):
#                 if board[x][y] == word[0]:
#                     if queue and (x == queue[-1][0] + 1 or y == queue[-1][1] + 1):
#                         pass
#                     else:
#                         queue.append((x, y, next_ch_idx))
#                         visited.add((x, y))
#
#         while queue:
#             x, y, next_ch_idx = queue.popleft()
#             for ne_x, ne_y in neighbours(x, y):
#                 queue.append((ne_x, ne_y, next_ch_idx + 1))
#                 visited.add((ne_x, ne_y))
#
#             if next_ch_idx == len(word):
#                 return True
#
#         return False
#     # [["C","A","A"],["A","A","A"],["B","C","D"]]
#     # "AAB"

# class Solution:
#     """
#     使用深度优先搜索：
#     1. 只需要求一个唯一解
#     2. 解的长度是固定的，因此在深的不大的情况下深度优先搜索和广度优先搜索的复杂度几乎相同
#     """
#
#     def exist(self, board: List[List[str]], word: str) -> bool:
#
#         def dfs(cur_x, cur_y, ch_idx):
#             if board[cur_x][cur_y] != word[ch_idx]:  # 如果当前数字和word不相符
#                 return False
#             if ch_idx == len(word) - 1:  # 如果数字相符，且已经达到了末尾
#                 return True
#
#             result = False
#             visited.add((cur_x, cur_y))
#             for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
#                 if 0 <= ne_x < len(board) and 0 <= ne_y < len(board[0]) and \
#                         (ne_x, ne_y) not in visited:  # 判断是否有遍历过
#                     if dfs(ne_x, ne_y, ch_idx + 1):
#                         result = True
#                         break
#
#             visited.remove((cur_x, cur_y))  # 在遍历完成之后要删除掉visited节点中的坐标，防止影响下次遍历
#             return result
#
#         m = len(board)
#         n = len(board[0])
#         visited = set()
#         for x in range(m):
#             for y in range(n):
#                 if dfs(x, y, 0):
#                     return True
#
#         return False


class Solution:
    def exist(self, board: List[List[str]], word: str):
        """
        使用深度优先搜索：
        1. 只需要求一个唯一解
        2. 解的长度是固定的，因此在深的不大的情况下深度优先搜索和广度优先搜索的复杂度几乎相同
        """
        def dfs(x, y, ch_idx):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[ch_idx]:
                # 检验非法情况（越界，数字不相等）
                return False
            if ch_idx == len(word) - 1:
                return True  # basecase, 此时默认board[x][y] == word[ch_idx]

            """
            下面是一个设置visited数组的小撇步，在每一次递归中将下一个要递归的元素用临时变量存起来
            并且在递归结束后复原
            （在调用栈出栈的时候会逐步吧所有更改过的元素复原）
            """
            tmp = board[x][y]
            board[x][y] = ''
            found = dfs(x + 1, y, ch_idx + 1) or \
                    dfs(x - 1, y, ch_idx + 1) or \
                    dfs(x, y + 1, ch_idx + 1) or \
                    dfs(x, y - 1, ch_idx + 1)
            """
            DFS搜寻相邻元素，只要有一个元素返回真即可
            PS. or 有短路性质，只要前一个为真，后面的元素就不再搜索
            """
            board[x][y] = tmp

            return found

        return any(dfs(x, y, 0) for x in range(len(board)) for y in range(len(board[0])))


test = Solution()
ret = test.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]],
                 "AAB")
print(ret)
