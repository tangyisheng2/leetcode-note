# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def nodeSum(node, remaining_sum):
            """
            This function returns the path sum from the selected root (or sub-root)
            """
            if not node:
                return 0

            remaining_sum -= node.val
            print(remaining_sum)
            if remaining_sum == 0:
                self.ans += 1

            nodeSum(node.left, remaining_sum)
            nodeSum(node.right, remaining_sum)

        if not root:
            return 0
        nodeSum(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.ans


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)

test = Solution()
ret = test.pathSum(root, 8)
