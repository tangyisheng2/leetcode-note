class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        走完一遍指令之后，如果满足以下条件之一，则表示机器人会在环内行走。
        1. 最后的位置在原始位置
        2. 最后的方向跟初始方向不同
        :param instructions:
        :return:
        """
        # direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 顺时针旋转的方向
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 前右后左方向移动一步坐标轴的变化
        heading = 0  # 目前的方向
        x, y = 0, 0  # 原点坐标
        for command in instructions:
            if command == "G":
                x += direction[heading][0]
                y += direction[heading][1]
            elif command == "L":
                heading = (heading - 1 + 4) % 4  # heading减1，+4后再余4是为了让heading保持在[0,3]的区间内
            else:
                heading = (heading + 1) % 4
        return [x, y] == [0, 0] or heading != 0


test = Solution()
ret = test.isRobotBounded(instructions="GGLLGG")
print(ret)
