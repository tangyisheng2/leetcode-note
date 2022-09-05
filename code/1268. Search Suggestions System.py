#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1268. Search Suggestions System.py
# @Time      :9/5/22
# @Author    :Eason Tang
from typing import List


# Trie tree node for storing word
class TireNode:
    def __init__(self):
        self.children = {}
        self.prefix_word = []


# Trie for searching
class Trie:
    def __init__(self):
        self.root = TireNode()  # 创建一个dummy节点

    def insert(self, word):
        """
        Insert the word to Trie
        :param word: word to Insert to the Trie
        :return:
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:  # 如果当前字母不在孩子节点中
                cur.children[ch] = TireNode()
            cur = cur.children[ch]  # 移动到下一个节点（此时可以认为我们已经插入）
            cur.prefix_word.append(word)  # 更新插入后节点的单词列表
            cur.prefix_word.sort()  # 更新单词排序，确保为字典序升序
            if len(cur.prefix_word) > 3:  # 如果超出3个元素
                cur.prefix_word.pop()

    def get(self, word):
        ans = []
        flag = False  # 提前结束标识位，如果搜索到一半已经没有结果，那继续搜索下去也不会有结果
        cur = self.root
        for ch in word:
            if flag or ch not in cur.children:  # 如果提前结束或当前字母不在孩子中
                ans.append([])  # 返回空结果
                flag = True  # 更新标识位
            else:
                cur = cur.children[ch]  # 移动当前指针到ch
                ans.append(cur.prefix_word)  # 更新结果
        return ans


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Insert to tree
        trie = Trie()
        for word in products:
            trie.insert(word)
        # Get Results
        return trie.get(searchWord)
