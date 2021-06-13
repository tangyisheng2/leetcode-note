import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        解题思路：
        题目中提到，只有与边界节点相连的节点才是不被"X"包围的节点
        因此我们从边界节点开始广度有限搜索，搜索所有相邻的节点
        并将这些节点置为"A"，说明这些节点与边界相连。
        最后遍历整个board，对所有不是"A"的节点置"X"（因为这些节点没有与边界节点相连）
        PS. 我们还可以使用visited数组的方式来存储节点（但是runtime稍长）
        执行用时: 60 ms 47%
        内存消耗: 18.3 MB 83%

        """
        def neighbours(cur_x, cur_y):
            for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
                if 0 <= ne_x < len(board) and 0 <= ne_y < len(board[0]) and board[ne_x][ne_y] == "O":
                    yield ne_x, ne_y

        queue = collections.deque()
        # visited = set()
        for i in range(len(board)): # 所有边界节点入队
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][len(board[0]) - 1] == "O":
                queue.append((i, len(board[0]) - 1))
        for i in range(len(board[0])):
            if board[0][i] == "O":
                queue.append((0, i))
            if board[len(board) - 1][i] == "O":
                queue.append((len(board) - 1, i))

        while queue:    # BFS
            node = queue.popleft()
            if board[node[0]][node[1]] == "O":
                board[node[0]][node[1]] = "A"   # 将与边界相连的节点数值改为A（后面会改回来，这里做标记用）
            for ne_node in neighbours(node[0], node[1]):
                queue.append(ne_node)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "A":  # "A": 与边界相连的饿节点
                    board[x][y] = "O"
                else:
                    board[x][y] = "X"   # 不与边界相连的节点置为X

        print(board)

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         """
#         解题思路：
#         题目中提到，只有与边界节点相连的节点才是不被"X"包围的节点
#         因此我们从边界节点开始广度有限搜索，搜索所有相邻的节点
#         并将这些节点置为"A"，说明这些节点与边界相连。
#         最后遍历整个board，对所有不是"A"的节点置"X"（因为这些节点没有与边界节点相连）
#         PS. 我们还可以使用visited数组的方式来存储节点
#         Visited方式：
#         runtime 68ms 29.10%
#         memory 18.2MB 82.99%
#         """
#
#         def neighbours(cur_x, cur_y):
#             for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
#                 if 0 <= ne_x < len(board) and 0 <= ne_y < len(board[0]) and board[ne_x][ne_y] == "O":
#                     yield ne_x, ne_y
#
#         queue = collections.deque()
#         visited = set()
#         for i in range(len(board)):
#             if board[i][0] == "O":
#                 queue.append((i, 0))
#                 visited.add((i, 0))
#             if board[i][len(board[0]) - 1] == "O":
#                 queue.append((i, len(board[0]) - 1))
#                 visited.add((i, len(board[0]) - 1))
#         for i in range(len(board[0])):
#             if board[0][i] == "O":
#                 queue.append((0, i))
#                 visited.add((0, i))
#             if board[len(board) - 1][i] == "O":
#                 queue.append((len(board) - 1, i))
#                 visited.add((len(board) - 1, i))
#
#         while queue:
#             node = queue.popleft()
#             if board[node[0]][node[1]] == "O" and board[node[0]][node[1]] not in visited:
#                 visited.add(node)
#             for ne_node in neighbours(node[0], node[1]):
#                 if ne_node not in visited:
#                     queue.append(ne_node)
#
#         for x in range(len(board)):
#             for y in range(len(board[0])):
#                 if board[x][y] == "O" and (x, y) not in visited:
#                     board[x][y] = "X"
#
#         print(board)


test = Solution()
test.solve([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
           )
# print(ret)
