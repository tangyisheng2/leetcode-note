#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :208. Implement Trie (Prefix Tree).py
# @Time      :10/24/21 4:51 PM
# @Author    :Eason Tang
class Trie:

    def __init__(self):
        """
        使用字典嵌套的方式来进行实现字典树（只有动态语言如Python可以实现这种方式）
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        插入字典树
        从前往后遍历插入单词的每一个字符，如果字符在字典树中存在，这继续遍历下一个，否则新建字典树节点
        :param word:
        :return:
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True  # 表示单词结尾

    def search(self, word: str) -> bool:
        """
        在字典树中查找单词
        从前往后遍历每一个字母，如果遍历到单词末尾并且结束字符#存在的时候返回真
        :param word:
        :return:
        """
        node = self.find(word)
        return node is not None and "#" in node

    def startsWith(self, prefix: str) -> bool:
        """
        在字典树中查找前缀
        从前往后遍历每一个字母，如果遍历到目标的前缀末尾则返回为真
        注意：这里不一定是要出现单词末尾
        :param prefix:
        :return:
        """
        return self.find(prefix) is not None

    def find(self, prefix):
        """
        查找固定前缀的开始节点（指针落在前缀末尾的字符）
        :param prefix:
        :return:
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
