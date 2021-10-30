"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
import collections
from typing import List


# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         def neighbours(cur_x, cur_y, visited):
#             for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
#                 if 0 <= ne_x < len(mat) and 0 <= ne_y < len(mat[0]) and \
#                         (ne_x, ne_y) not in visited:
#                     yield ne_x, ne_y
#
#         def bfs(x, y):
#             queue = collections.deque()
#             queue.append((x, y, 0))
#             visited = set()
#             visited.add((x, y))
#
#             while queue:
#                 cur_x, cur_y, cnt = queue.popleft()
#                 if mat[cur_x][cur_y] == 0:
#                     res[x][y] = cnt
#                     break  # 提前剪枝，由队列的FIFO特性可知该节点就是离头节点最近的0节点
#                 for ne_x, ne_y in neighbours(cur_x, cur_y, visited):
#                     queue.append((ne_x, ne_y, cnt + 1))  # 邻居节点的距离比当前节点多一
#                     visited.add((ne_x, ne_y))
#
#         import numpy
#         res = []
#         for row in range(len(mat)):
#             res.append([0] * len(mat[0]))  # 创建一个和mat相同维度的数组
#         for x in range(len(mat)):
#             for y in range(len(mat[0])):
#                 if mat[x][y] == 0:
#                     res[x][y] = 0  # 如果是0则距离直接为0
#                 else:
#                     bfs(x, y)  # 否则进行BFS寻找最近的0
#         return res

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        import collections

        def bfs(mat, x, y):
            q = collections.deque([(x, y, 0)])
            visited = {(x, y)}

            while q:
                cur_x, cur_y, distance = q.popleft()
                if mat[cur_x][cur_y] == 0:
                    ans[x][y] = distance
                    break
                for ne_x, ne_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

                    if 0 <= ne_x < m and 0 <= ne_y < n and (ne_x, ne_y) not in visited:
                        q.append((ne_x, ne_y, distance + 1))
                        visited.add((ne_x, ne_y))

        m, n = len(mat), len(mat[0])
        ans = [[-1] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                bfs(mat, x, y)
        return ans


test = Solution()
# ret = test.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
ret = test.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print(ret)
