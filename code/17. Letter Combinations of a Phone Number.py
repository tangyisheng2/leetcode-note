#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :17. Letter Combinations of a Phone Number.py
# @Time      :10/16/21 11:16 PM
# @Author    :Eason Tang
from typing import List

# DFS
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         def dfs(digits, digit_ch_mapping, solved_digit, current_stat, ans):
#             """
#             一般我们习惯输入放前面，中间变量放中间，最后放输出变量
#             :param digits: 输入字符串
#             :param digit_ch_mapping: mapping的dict
#             :param solved_digit: 当前已经求解多少位
#             :param current_stat: 从root走到当前节点经历的边
#             :param ans: 输出的ans
#             :return:
#             """
#             if solved_digit == len(digits):
#                 if solved_digit > 0:
#                     ans.append("".join(current_stat))
#                 return  # 因为每一次结束我们将新增结果到ans
#
#             for c in digit_ch_mapping[ord(digits[solved_digit]) - ord('0')]:
#                 current_stat[solved_digit] = c
#                 dfs(digits, digit_ch_mapping, solved_digit + 1, current_stat, ans)
#
#         ch = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]  # 数字和字母的mapping关系
#         cur = [' ' for _ in range(len(digits))]  # 总共每一位的长度
#         ans = []  # 最后返回结果
#         dfs(digits, ch, 0, cur, ans)
#         return ans


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]  # 数字和字母的mapping关系
        ans = [""]  # 初始结果是dummy result
        for digit in digits:
            tmp = []
            for s in ans:   # 遍历已经存在的结果
                for c in d[ord(digit) - ord("0")]:  # 分别往结果的后面加单词
                    tmp.append(s + c)
            ans = tmp   # 将已经添加的结果拷贝过去
        return ans


test = Solution()
test.letterCombinations("23")
