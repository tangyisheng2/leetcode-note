import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def neighbours(cur_x, cur_y):
            for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
                if 0 <= ne_x < len(board) and 0 <= ne_y < len(board[0]) and board[ne_x][ne_y] == "O":
                    yield ne_x, ne_y

        def bfs(x, y):
            queue = collections.deque()
            queue.append((x, y))
            visited = set()
            visited.add((x, y))
            have_boarder_element = False
            while queue:
                node = queue.popleft()
                cur_x, cur_y = node
                if cur_x == 0 or cur_x == len(board) - 1 or \
                        cur_y == 0 or cur_y == len(board[0]) - 1:   # 判断是否有刚好在边界的节点
                    have_boarder_element = True  # 如果是边界节点则返回所有与边界节点相连的集合

                for node in neighbours(cur_x, cur_y):
                    if node not in visited:
                        queue.append(node)
                        visited.add(node)

            if not have_boarder_element:
                for node in visited:
                    board[node[0]][node[1]] = "X"

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    bfs(x,y)


        pass


test = Solution()
test.solve([["X","O","X"],["O","X","O"],["X","O","X"]]
)
# print(ret)
