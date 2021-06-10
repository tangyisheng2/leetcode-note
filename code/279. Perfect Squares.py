"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 104
"""
import collections
import math


class Solution:
    def numSquares(self, n: int) -> int:
        """
        DP
        :param n: target
        :return: minimum square number needed to sum target
        """
        square_numbers = [pow(x, 2) for x in range(1, int(math.sqrt(n)) + 1)]
        dp_table = [-1] * (n + 1)
        dp_table[0] = 0
        for num in square_numbers:
            dp_table[num] = 1
        # 以上构建初始DP表
        curIdx = 0
        while curIdx <= n:
            for num in square_numbers:
                if curIdx + num < len(dp_table) and \
                        (dp_table[curIdx + num] == -1 or dp_table[curIdx] + 1 < dp_table[curIdx + num]):
                    dp_table[curIdx + num] = dp_table[curIdx] + 1
            curIdx += 1

        return dp_table[n]


# class Solution:
#     def numSquares(self, n: int) -> int:
#         """
#         DP
#         :param n: target
#         :return: minimum square number needed to sum target
#         """
#         min_sqrt_num = n + 1
#         square_numbers = [pow(x, 2) for x in range(1, int(math.sqrt(n)) + 1)]
#         queue = collections.deque()
#         for num in square_numbers:
#             queue.append((n, 0))  # (当前的sum，目前使用的num)
#
#         while queue:
#             cur_sum, cnt = queue.popleft()
#             if cur_sum == 0:
#                 min_sqrt_num = min(min_sqrt_num, cnt)
#             if cur_sum < 0:
#                 continue
#             for num in square_numbers:
#                 remainder = cur_sum - num
#                 if remainder >= 0:
#                     queue.append((remainder, cnt + 1))
#
#         return min_sqrt_num


test = Solution()
ret = test.numSquares(12)
print(ret)
