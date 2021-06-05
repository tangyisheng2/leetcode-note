"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:
Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


# class Solution:
#     def countNodes(self, root) -> int:
#         """
#         BFS
#         :param root: 根节点
#         :return: 孩子数量
#         """
#         if not root:  # 空树
#             return 0
#         count = 1  # 如果不是空树，则至少又一个根节点（root）
#         q = collections.deque()  # 初始化队列
#         q.append(root)  # 根节点入队
#         while q:
#             node = q.popleft()
#             if node.left:  # 左孩子
#                 count += 1
#                 q.append(node.left)
#             if node.right:  # 右孩子
#                 count += 1
#                 q.append(node.right)
#         return count


class Solution:
    def countNodes(self, root) -> int:
        def calcTreeheight(root):
            """
            计算树高
            :param root:
            :return:
            """
            if not root:
                return 0
            count = 0
            while root.left:
                root = root.left
                count += 1
            return count

        def isNodeexist(node, node_id):
            """
            确定节点是否存在
            :param node:
            :param node_id:
            :return:
            """

            bin_code = [ch for ch in bin(node_id).split("b")[1]]

            for index in range(1, len(bin_code)):
                if not node:
                    return False
                if bin_code[index] == "0":
                    node = node.left
                elif bin_code[index] == "1":
                    node = node.right

            return True if node else False

        if not root:
            return 0
        height = calcTreeheight(root)
        lo = int(pow(2, height))
        hi = int(pow(2, height + 1)) - 1
        mid = (lo + hi) // 2  # 对mid赋初值防止undefined min
        while lo <= hi:
            mid = (lo + hi) // 2  # 更新mid中间值
            if isNodeexist(root, mid - 1) and not isNodeexist(root, mid):  # 如果树不是完全二叉树，则通过判断边界来确定节点数量
                return mid - 1
            if isNodeexist(root, mid):  # 如果监测到节点存在，则边界在mid右边
                lo = mid + 1
            elif not isNodeexist(root, mid):  # 如果检测到节点不存在，则边界在节点左边
                hi = mid - 1
        return mid  # 当满二叉树时，mid到最右边节点，直接return mid


root = TreeNode(val=0)
root.left = TreeNode(val=1)
root.right = TreeNode(val=2)

test = Solution()
test.countNodes(root)
