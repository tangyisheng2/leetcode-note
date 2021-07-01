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


class Solution:
    def __init__(self):
        self.memo = {}  # 初始化memo

    def climbStairs(self, n: int) -> int:
        self.memo = {}  # 每一次运行之前把memo清空
        return self.goClimb(n)

    def goClimb(self, n):
        if n in self.memo:  # hit memo
            return self.memo[n]
        if n == 0 or n == 1:    # basecase
            return 1
        self.memo[n - 1] = self.goClimb(n - 1)
        self.memo[n - 2] = self.goClimb(n - 2)
        return self.memo[n - 1] + self.memo[n - 2]


test = Solution()
ret = test.climbStairs(5)
print(ret)
