# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   729. My Calendar I.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


# from sortedcontainers import sortedlist
#
#
# class MyCalendar(object):
#     def __init__(self):
#         self.s = sortedlist.SortedList()
#
#     def book(self, start, end):
#         event = (start, end)
#         index = self.s.bisect_left(event)
#         if index > 0 and start < self.s[index - 1][1] or index < len(self.s) and end > self.s[index][0]:
#             # index > 0 和index < len(self.s) 用来防止数组越界
#             # start < self.s[index - 1][1] 开始时间 < 上一个event的结束时间
#             # end > self.s[index][0] 结束时间 > （插入后的下一个）event的开始时间
#             return False
#         else:
#             self.s.add(event)
#             return True

class Node:
    """
    平衡术树节点，左边小，又变大
    """
    __slots__ = 'start', 'end', 'left', 'right'

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        """
        插入节点：
        反例：[1, 5), [7, 10), [5, 8)
        最后一个无法插入
        :param node:
        :return:
        """
        if node.start >= self.end:  # 开始晚于节点结束（Valid）
            if not self.right:  # 如果没有右孩子直接添加
                self.right = node
                return True
            return self.right.insert(node)  # 否则递归寻找
        elif node.end <= self.start:    # 结束早于节点开始（Valid）
            if not self.left:   # 如果没有左孩子直接添加
                self.left = node
                return True
            return self.left.insert(node)   # 否则递归查找
        else:
            return False


class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

if __name__ == '__main__':
    ops = ["MyCalendar", "book", "book", "book", "book"]
    datas = [[], [1, 2], [3, 4], [7, 10], [5, 6]]
    for op, data in zip(ops, datas):
        if op == "MyCalendar":
            cal = MyCalendar()
        elif op == "book":
            cal.book(data[0], data[1])
    pass
