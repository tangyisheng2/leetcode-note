# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   22. Generate Parentheses.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        动态规划：
        dp[i]表示i组括号的所有有效组合
        dp[i] = "(dp[p]的所有有效组合)+【dp[q]的组合】"，其中 1 + p + q = i , p从0遍历到i-1, q则相应从i-1到0
        """

        dp = [[] for _ in range(n + 1)]  # dp[i]存放i组括号的所有有效组合
        dp[0] = [""]  # 初始化dp[0]
        for i in range(1, n + 1):  # 计算dp[i]
            for p in range(i):  # 遍历p
                inside_parentheses_list = dp[p]  # 得到dp[p]的所有有效组合，放在()内
                outside_parentheses_list = dp[i - 1 - p]  # 得到dp[q]的所有有效组合，放在()右边
                for inside_parentheses in inside_parentheses_list:
                    for outside_parentheses in outside_parentheses_list:
                        dp[i].append(f'({inside_parentheses}){outside_parentheses}')

        return dp[n]


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#
#         res = []
#         cur_str = ''
#
#         def dfs(cur_str, left, right, n):
#             """
#             :param cur_str: 从根结点到叶子结点的路径字符串
#             :param left: 左括号已经使用的个数
#             :param right: 右括号已经使用的个数
#             :return:
#             """
#             if left == n and right == n:
#                 res.append(cur_str)
#                 return
#             if left < right:
#                 return
#
#             if left < n:
#                 dfs(cur_str + '(', left + 1, right, n)
#
#             if right < n:
#                 dfs(cur_str + ')', left, right + 1, n)
#
#         dfs(cur_str, 0, 0, n)
#         return res


if __name__ == '__main__':
    ret = Solution().generateParenthesis(3)
