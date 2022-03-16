#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :432. All O`one Data Structure.py
# @Time      :3/15/22
# @Author    :Eason Tang


class AllOne:
    def __init__(self):
        from sortedcontainers import SortedDict
        from collections import defaultdict
        self.wordnums = defaultdict(int)  # 计数
        self.numsword = SortedDict()  # 按照key升序排序的字典

    def inc(self, key: str) -> None:
        self.wordnums[key] += 1  # 当前计数 +1
        if self.wordnums[key] > 1:  # 如果之前已经存在这个key
            self.removeinnumsword(self.wordnums[key] - 1, key)  # 则删除当前节点
        self.add2numsword(key, self.wordnums[key])  # 重新插入节点（更新计数21）

    def dec(self, key: str) -> None:
        self.removeinnumsword(self.wordnums[key], key)  # 删除原来count为n的key
        self.wordnums[key] -= 1  # 计数 -1
        if self.wordnums[key]:  # 如果计数不为0
            self.add2numsword(key, self.wordnums[key])  # 则在新位置插入节点

    def getMaxKey(self) -> str:
        res = ""
        if self.numsword.keys():  # 如果链表不为空
            res = self.numsword[self.numsword.keys()[-1]].pop()  # 返回res
            self.numsword[self.numsword.keys()[-1]].add(res)  # 将pop的key放回去
        return res

    def getMinKey(self) -> str:
        res = ""
        if self.numsword.keys():
            res = self.numsword[self.numsword.keys()[0]].pop()  # 返回res
            self.numsword[self.numsword.keys()[0]].add(res)  # 将pop的key放回去
        return res

    def add2numsword(self, key, n):
        if n in self.numsword:  # 如果已经存在count为n的节点
            self.numsword[n].add(key)  # 则直接在该节点加入key
        else:
            self.numsword[n] = set([key])  # 否则新建节点

    def removeinnumsword(self, n, key):
        self.numsword[n].remove(key)  # 在count为n的节点中去除key
        if not self.numsword[n]:  # 如果count为n的链表节点已经空了
            self.numsword.pop(n)

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
