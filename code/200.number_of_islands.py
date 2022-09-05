from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            grid[x][y] = '0'

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                    dfs(nx, ny)

        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans


test_case = Solution()
input = [
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
]
for data_input in input:
    test_case.numIslands(data_input)