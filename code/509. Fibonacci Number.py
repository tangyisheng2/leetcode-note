"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

"""


# class Solution:
#     memo = {}
#
#     def fib(self, n: int) -> int:
#         """
#         带memo的DP解法
#         :param n:
#         :return:
#         """
#         if n < 2:   # 特殊情况判定
#             self.memo[n] = 1
#             return n
#         if n in self.memo:
#             return self.memo[n]
#
#         self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
#         return self.memo[n]

class Solution:
    def fib(self, n: int) -> int:
        """
        DP_table
        :param n:
        :return:
        """
        if n == 0:  # 1. 确定base case
            return 0
        if n == 1:
            return 1

        dp = [0 for _ in range(n + 1)]  # 建表
        dp[0] = 0  # 确定初始值
        dp[1] = 1

        for i in range(2, n + 1):  # 2. 确定会变化的状态
            dp[i] = dp[i - 1] + dp[i - 2]  # 3. 确定选择，更新DP表

        return dp[n]  # 4. 得到答案


test = Solution()
for i in range(256):
    print(f'{i}:{test.fib(i)}')
