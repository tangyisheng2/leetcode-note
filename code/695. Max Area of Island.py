class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def isInArea(grid, x, y):
            """
            判断是否在区域内
            """
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                return True
            else:
                return False

        def dfs(grid, x, y):
            """
            DFS遍历
            """
            if not isInArea(grid, x ,y):
                return 0 #判断越界
            if grid[x][y] != "1":   
                # 如果该地区不是陆地（包括0，以及2已经便利过的情况）
                # 还有注意数据类型是str还是int
                return 0
            grid[x][y] = "0"
            space_count = 1
            space_count += dfs(grid, x + 1, y, space_count)
            space_count += dfs(grid, x - 1, y, space_count)
            space_count += dfs(grid, x, y + 1, space_count)
            space_count += dfs(grid, x, y - 1, space_count)
            return space_count

        max_space = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    max_space = max(max_space, dfs(grid, x, y))
        return max_space
                        
