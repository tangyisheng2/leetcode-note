#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :211. Design Add and Search Words Data Structure.py
# @Time      :3/26/22
# @Author    :Eason Tang


class WordDictionary:
    """
    We use a trie
    Add would be normal

    When we search a ".", initialize dfs on this node, return any possible results
    """

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch in node:
                node = node[ch]
            else:
                node[ch] = {}
                node = node[ch]
        node['#'] = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        def dfs(node, s):
            """
            Use DFS to traverse the tree, and optimize using early stop
            """
            nonlocal early_stop
            if early_stop:  # If found result, do early stop
                return True

            for i, ch in enumerate(s):
                # Case1: do fuzzy search when encounter "."
                if ch == '.':
                    for ne in node.keys():
                        if ne != '#':
                            if dfs(node[ne], s[i + 1:]):
                                return True
                    return False
                # Case2: do exact search, but not found
                if ch not in node:
                    return False
                # Case3: Do exact search and found
                node = node[ch]
            early_stop = '#' in node
            return early_stop

        early_stop = False
        return dfs(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
print(obj.addWord("bad"))
print(obj.addWord("dad"))
print(obj.addWord("mad"))
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
