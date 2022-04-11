#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :173. Binary Search Tree Iterator.py
# @Time      :4/11/22
# @Author    :Eason Tang


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    预处理：先使用中序遍历获得遍历后的数组，然后对该数组使用指针实现迭代器
    """

    def __init__(self, root: TreeNode):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.q.append(root.val)
            inorder(root.right)

        self.q = []
        self.ptr = -1
        inorder(root)
        print(self.q)

    def next(self) -> int:
        if self.hasNext():
            self.ptr += 1
            ans = self.q[self.ptr]
            return ans

    def hasNext(self) -> bool:
        return self.ptr + 1 < len(self.q)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
