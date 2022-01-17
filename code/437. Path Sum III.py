# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def __init__(self):
#         self.ans = 0
#
#     def pathSum(self, root: TreeNode, targetSum: int) -> int:
#         def nodeSum(node, remaining_sum):
#             """
#             This function returns the path sum from the selected root (or sub-root)
#             """
#             if not node:
#                 return 0
#
#             remaining_sum -= node.val
#             print(remaining_sum)
#             if remaining_sum == 0:
#                 self.ans += 1
#
#             nodeSum(node.left, remaining_sum)
#             nodeSum(node.right, remaining_sum)
#
#         if not root:
#             return 0
#         nodeSum(root, targetSum)
#         self.pathSum(root.left, targetSum)
#         self.pathSum(root.right, targetSum)
#         return self.ans

# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> int:
#         import collections
#         prefix = collections.defaultdict(int)
#         # prefix[0] = 1
#
#         def dfs(root, curr):
#             """
#             记录下根节点 root 到当前节点 p 的路径上除当前节点以外所有节点的前缀和，
#             在已保存的路径前缀和中查找是否存在前缀和刚好等于当前节点到根节点的前缀和 curr - targetSum
#             :param root: 根结点
#             :param curr: 从根结点到当前节点node的前缀和
#             :return:
#             """
#             if not root:
#                 return 0
#
#             ret = 0  # 对于空路径，前缀和为0
#             curr += root.val  # 更新前缀和
#             ret += prefix[curr - targetSum]  # 寻找是否存在解答
#
#             # Backtracking
#             prefix[curr] += 1  # 更新前缀和
#             ret += dfs(root.left, curr)  # 递归
#             ret += dfs(root.right, curr)
#             prefix[curr] -= 1  # 状态复原
#
#             return ret
#
#         return dfs(root, 0)


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root, curr):
            """
            记录下根节点 root 到当前节点 p 的路径上除当前节点以外所有节点的前缀和，
            在已保存的路径前缀和中查找是否存在前缀和刚好等于当前节点到根节点的前缀和 curr - targetSum
            :param root: 根结点
            :param curr: 从根结点到当前节点node的前缀和
            :return:
            """
            nonlocal ans
            if not root:
                return 0

            # ans = 0  # 对于空路径，前缀和为0
            curr += root.val  # 更新前缀和
            ans += prefix[curr - targetSum]  # 寻找是否存在解答

            # Backtracking
            prefix[curr] += 1  # 更新前缀和
            ans += dfs(root.left, curr)  # 递归
            ans += dfs(root.right, curr)
            prefix[curr] -= 1  # 状态复原

            return ans
        import collections
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        ans = 0
        dfs(root, 0)
        return ans

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
