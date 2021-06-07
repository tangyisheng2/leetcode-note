"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""
import collections


class Solution:
    def orangesRotting(self, grid: list) -> int:
        """
        观察到对于所有的腐烂橘子，其实它们在广度优先搜索上是等价于同一层的节点的。
        因此我们使用timestamp来标记同一层腐烂的橘子，并同时对他们进行BFS
        :param grid:
        :return:
        """

        def neighbour(x, y):
            for r, c in [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]:
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    yield r, c

        queue = collections.deque()
        timestamp = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append((x, y, 0))

        while queue:
            x, y, timestamp = queue.popleft()
            for r, c in neighbour(x, y):
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    queue.append((r, c, timestamp + 1))

        if any(1 in row for row in grid):
            return -1

        return timestamp


test = Solution()
ret = test.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(ret)
