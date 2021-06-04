class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isInArea(grid, x, y):
            if (x >= 0 and x <= len(grid) and
                    y >= 0 and y <= len(grid[1])):  # 判断是否越界
                return True
            else:
                return False

        def dfs(grid, x, y):
            if (not isInArea()) or grid[x][y] != 1:  # 如果越界或者该地区不是陆地（包括0，以及2已经便利过的情况）
                return
            grid[x][y] = 2
            dfs(grid, x + 1, y)
            dfs(grid, x - 1, y)
            dfs(grid, x, y + 1)
            dfs(grid, x, y - 1)

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[1])):
                if grid[x][y] == 1:
                    count += 1
                    dfs(grid, x, y)
        return count


test_case = Solution()
input = [
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
]
for data_input in input:
    test_case.numIslands(data_input)