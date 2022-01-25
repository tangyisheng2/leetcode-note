#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :449. Serialize and Deserialize BST.py
# @Time      :1/24/22
# @Author    :Eason Tang


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def dfs(root):
            if not root:
                ans.append(None)
                return

            ans.append(root.val)

            dfs(root.left)
            dfs(root.right)

        ans = []
        dfs(root)
        return ",".join(map(str, ans))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def dfs(root):
            nonlocal cur_node_cnt
            if not root:
                return []

            if cur_node_cnt >= len(data):
                return

            if data[cur_node_cnt] != "None":
                root.left = TreeNode(data[cur_node_cnt])
            cur_node_cnt += 1
            dfs(root.left)

            if data[cur_node_cnt] != "None":
                root.right = TreeNode(data[cur_node_cnt])
            cur_node_cnt += 1
            dfs(root.right)

        data = data.split(",")
        if data[0] == "None":
            return []
        root = TreeNode(data[0])
        cur_node_cnt = 1

        dfs(root)

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
