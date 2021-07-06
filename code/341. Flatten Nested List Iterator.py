# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   341. Flatten Nested List Iterator.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng

@Modify Time        @Author     @Version        @Description
------------        -------     --------        -----------
2021/7/6     tangyisheng2        1.0             数据库链接
"""

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
#
#
# class NestedInteger:
#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """
#
#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """
#
#     def getList(self) -> [NestedInteger]:
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in reversed(range(len(nestedList))):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self) -> bool:
        """
        在构造函数中应该初始化，把当前列表的各个元素（不用摊平）逆序放入栈中。
        在 hasNext()方法中，访问（不弹出）栈顶元素，判断是否为 int：
        如果是 int 那么说明有下一个元素，返回 true；然后 next() 就会被调用，把栈顶的 int 弹出；
        如果是 list 需要把当前列表的各个元素（不用摊平）逆序放入栈中。
        如果栈为空，那么说明原始的嵌套列表已经访问结束了，返回 false。
        :return:
        """
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in reversed(range(len(cur.getList()))):
                self.stack.append(cur.getList()[-i])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
