from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        单向BFS
        :param grid:
        :return:
        """
        def neighbours(node):
            x, y = node
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1),
                           (x - 1, y + 1), (x - 1, y - 1)]:
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and \
                        (nx, ny) not in visited and \
                        grid[nx][ny] == 0:
                    yield nx, ny

        start = (0, 0)
        end = (len(grid) - 1, len(grid[0]) - 1)

        if grid[start[0]][start[1]] == 1:  # 判断开始非法情况
            return -1

        step = 1  # 开始时已经算第一步
        visited = set()
        queue = collections.deque()
        queue.append((start, step))
        visited.add(start)

        while queue:
            # BFS
            cur_node, step = queue.popleft()
            if cur_node == end:  # 当检测到达终点的时候停止
                return step
            for nx, ny in neighbours(cur_node):
                queue.append(((nx, ny), step + 1))
                visited.add((nx, ny))
        return -1  # 尝试所有方式后无法到达


test = Solution()
ret = test.shortestPathBinaryMatrix([[0, 1], [1, 0]])
print(ret)
