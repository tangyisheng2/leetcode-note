# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   70. Climbing Stairs.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng

@Modify Time        @Author     @Version        @Description
------------        -------     --------        -----------
2021/7/1     tangyisheng2        1.0             数据库链接
"""


# class Solution:
#     def __init__(self):
#         self.memo = {}  # 初始化memo
#
#     def climbStairs(self, n: int) -> int:
#         self.memo = {}  # 每一次运行之前把memo清空
#         return self.goClimb(n)
#
#     def goClimb(self, n):
#         if n in self.memo:  # hit memo
#             return self.memo[n]
#         if n == 0 or n == 1:    # basecase
#             return 1
#         self.memo[n - 1] = self.goClimb(n - 1)
#         self.memo[n - 2] = self.goClimb(n - 2)
#         return self.memo[n - 1] + self.memo[n - 2]

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            # 走i层楼梯的步数 = 走i - 2层后再跨两层 + i - 1层后再跨1层的步数
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


test = Solution()
ret = test.climbStairs(5)
print(ret)
