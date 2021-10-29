#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :212. Word Search II.py
# @Time      :10/24/21 12:00 PM
# @Author    :Eason Tang
from typing import List

# class Solution:
#     """
#     Solution1: 对于每一个单词进行搜索（超时）
#     """
#
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         def dfs(x, y, ch_index):
#             if x < 0 or x == len(board) or y < 0 or y == len(board[0]) or board[x][y] != word[ch_index]:
#                 return False
#
#             if ch_index == len(word) - 1:
#                 return True
#
#             cur = board[x][y]
#             board[x][y] = ''
#             found = dfs(x + 1, y, ch_index + 1) or \
#                     dfs(x - 1, y, ch_index + 1) or \
#                     dfs(x, y + 1, ch_index + 1) or \
#                     dfs(x, y - 1, ch_index + 1)
#             board[x][y] = cur
#
#             return found
#
#         ans = []
#         for word in words:
#             if any(dfs(x, y, 0) for x in range(len(board)) for y in range(len(board[0]))):
#                 ans.append(word)
#         return ans

from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True  # 单词结束标志位
        cur.word = word  # 存储当前节点结束的单词


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:  # 构建前缀树
            root.insert(word)

        def dfs(node, x, y):
            if board[x][y] not in node.children:  # 如果节点不在前缀树中
                return

            ch = board[x][y]  # 如果在前缀树中就移动到下一个节点
            node = node.children[ch]

            if node.word != "":  # 检查是否为叶子结点
                ans.add(node.word)

            board[x][y] = "#"

            for ne_x, ne_y in [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]:
                if 0 <= ne_x < len(board) and 0 <= ne_y < len(board[0]):
                    dfs(node, ne_x, ne_y)
            board[x][y] = ch

        ans = set()
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(root, x, y)
        return list(ans)
