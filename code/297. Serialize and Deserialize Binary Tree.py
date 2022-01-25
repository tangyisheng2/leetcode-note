#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :297. Serialize and Deserialize Binary Tree.py
# @Time      :1/17/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        Do a pre-order tree traversal, and then append each node
        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            if not node:
                ans.append("None")
                # When we have a None node, we append node to mark the node does not exist, and when we deserialize it,
                # we also check if node is None to skip the branch
                return

            ans.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        ans = []
        dfs(root)
        print(",".join(ans))
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        Do a pre-order traversal, at the mean time we traverse through each node.
        When going through each node, we check if the node is none, if yes, we skip that node
        :type data: str
        :rtype: TreeNode
        """

        def dfs(node):
            """
            This function return the deserialized tree

            """
            nonlocal cur_node_cnt
            if not node:
                return

            if cur_node_cnt >= len(node_list):
                return

            if node_list[cur_node_cnt] != "None":
                node.left = TreeNode(node_list[cur_node_cnt])
            cur_node_cnt += 1
            dfs(node.left)

            if node_list[cur_node_cnt] != "None":
                node.right = TreeNode(node_list[cur_node_cnt])
            cur_node_cnt += 1
            dfs(node.right)

        print(data)
        node_list = data.split(",")
        if node_list[0] == "None":
            return []

        root = TreeNode(int(node_list[0]))
        cur_node_cnt = 1
        dfs(root)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

deser = Codec()
ret = deser.deserialize("1,2,None,None,3,4,None,None,5,None,None")