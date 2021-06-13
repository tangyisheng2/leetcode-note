# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        判定两个节点是cousin节点的重要条件是：
        1. 具有相同的深度
        2. 他们的父节点不同
        :param root:
        :param x:
        :param y:
        :return:
        """
        queue = collections.deque()
        # queue: (node, depth, parents)
        queue.append((root, 0, None))
        res_x, res_y = None, None
        while queue:
            node, depth, parents = queue.popleft()
            if node.val == x:   # 找到X
                res_x = (node, depth, parents)
            if node.val == y:   # 找到Y
                res_y = (node, depth, parents)
            if res_x and res_y is not None and \
                    res_x[1] == res_y[1] and \
                    res_x[2] != res_y[2]:
                # 判断是否是cousin节点：depth相同，parent不同
                return True
            if node.left is not None:
                queue.append((node.left, depth + 1, node.val))
            if node.right is not None:
                queue.append((node.right, depth + 1, node.val))

        return False
