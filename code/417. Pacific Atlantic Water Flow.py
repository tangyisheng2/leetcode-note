"""
You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.


Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]

Constraints:
m == heights.length
n == heights[i].length
1 <= m, n <= 200
0 <= heights[i][j] <= 105
https://leetcode-cn.com/problems/pacific-atlantic-water-flow/solution/bfspython3-by-westqi-qqz3/
"""
import collections
from typing import List


# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         def BFS(start):
#             """
#             BFS搜索
#             :param start:
#             :return:
#             """
#             queue = collections.deque()
#             queue.append(start)
#             visited = set()
#             visited.add(start)
#             canFlowAtlantic = 0  # 用于检测是否到达大西洋
#             canFlowPacific = 0  # 用于检测是否到达太平洋
#             while queue:
#                 nx, ny = queue.popleft()
#                 for x, y in [(nx + 1, ny), (nx, ny + 1), (nx - 1, ny), (nx, ny - 1)]:
#                     if 0 <= x < len(heights) and 0 <= y < len(heights[0]) \
#                             and heights[x][y] <= heights[nx][ny] and (x, y) not in visited:
#                         # 判断三个条件
#                         # 1. 是否越界
#                         # 2. 是否周边节点比本身笑
#                         # 3. 是否已经遍历过
#                         queue.append((x, y))
#                         visited.add((x, y))
#
#                 if nx == 0 or ny == 0:
#                     canFlowPacific = 1
#                 if nx == len(heights) - 1 or ny == len(heights[0]) - 1:
#                     canFlowAtlantic = 1
#                 if canFlowAtlantic == 1 and canFlowPacific == 1:
#                     return True
#             return False
#
#         # print(BFS((1,4)))
#         res = []
#         for i in range(len(heights)):
#             for j in range(len(heights[0])):
#                 if BFS((i, j)):
#                     res.append((i, j))
#         return res


# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         def BFS(x, y, visited):
#             """
#             返回visited表示所有遍历过的节点(有BUG)
#             :param visited:
#             :param x:
#             :param y:
#             :return:
#             """
#
#             queue = collections.deque()
#             queue.append((x, y))
#
#             while queue:
#                 node_x, node_y = queue.popleft()
#                 for neighbour_x, neighbour_y in [(node_x + 1, node_y),
#                                                  (node_x - 1, node_y),
#                                                  (node_x, node_y + 1),
#                                                  (node_x, node_y - 1)]:
#                     if 0 <= neighbour_x < len(heights) and 0 <= neighbour_y < len(heights) and \
#                             heights[neighbour_x][neighbour_y] >= heights[node_x][node_y] and \
#                             (neighbour_x, neighbour_y) not in visited:
#                         queue.append((neighbour_x, neighbour_y))
#                         visited.add((neighbour_x, neighbour_y))
#
#             # return visited
#
#         visited_pacific = set()
#         visited_atlantic = set()
#         for x in range(len(heights)):
#             BFS(x, 0, visited_pacific)
#             # visited_pacific.add((x, 0))
#             BFS(x, len(heights[0]) - 1, visited_atlantic)
#             # visited_atlantic.add((x, len(heights[0]) - 1))
#         for y in range(len(heights[0])):
#             BFS(0, y, visited_pacific)
#             # visited_pacific.add((0,y))
#             BFS(len(heights) - 1, y, visited_atlantic)
#             # visited_atlantic.add((len(heights) - 1))
#
#         return list(visited_pacific & visited_atlantic)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def BFS(x, y, visited):

            queue = collections.deque()
            queue.append((x, y))
            visited.add((x, y))

            def neighbours(node):
                x, y = node
                for neighbour_x, neighbour_y in [(x + 1, y),
                             (x - 1, y),
                             (x, y + 1),
                             (x, y - 1)]:
                    if 0 <= neighbour_x < m and 0 <= neighbour_y < n and \
                            heights[neighbour_x][neighbour_y] >= heights[x][y] and \
                            (neighbour_x, neighbour_y) not in visited:
                        # 检查越界、检查大小、检查是否遍历
                        # 水往高处流
                        yield neighbour_x, neighbour_y

            while queue:
                node = queue.popleft()
                for neighbour_node in neighbours(node):
                    queue.append(neighbour_node)
                    visited.add(neighbour_node)

        m, n = len(heights), len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()
        for x in range(m):
            BFS(x, 0, visited_pacific)
            BFS(x, n - 1, visited_atlantic)
        for y in range(n):
            BFS(0, y, visited_pacific)
            BFS(m - 1, y, visited_atlantic)
        return list(visited_pacific & visited_atlantic)



test = Solution()
ret = test.pacificAtlantic(
    [[1, 1], [1, 1], [1, 1]])
print(ret)
