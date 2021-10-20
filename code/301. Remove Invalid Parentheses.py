#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :301. Remove Invalid Parentheses.py
# @Time      :10/20/21 1:18 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for ch in s:  # 计算左括号与右括号的匹配程度
                if ch == '(':
                    count += 1
                if ch == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def dfs(s, begin_idx, l, r, ans):
            """

            :param s: 字符串
            :param begin_idx: 开始删除的idx
            :param l: 剩余要删除的左括号
            :param r: 剩余要删除的右括号
            :param ans:
            :return:
            """
            if l == 0 and r == 0:  # 如果已经平衡
                if isValid(s):  # 保底检查一下是不是valid字符串
                    ans.append(s)
                return

            for i in range(begin_idx, len(s)):
                if i > begin_idx and s[i] == s[i - 1]:  # 去除重复
                    continue

                if s[i] == '(' or s[i] == ')':
                    # cur = s
                    # cur.pop(i)
                    cur = f'{s[:i]}{s[i + 1:]}'  # 去除某一括号
                    if r > 0:  # 去除左括号
                        dfs(cur, i, l, r - 1, ans)
                    elif l > 0:  # 去除右括号
                        dfs(cur, i, l - 1, r, ans)

        l = 0
        r = 0

        for ch in s:
            l += (ch == '(')
            if (l == 0):
                r += (ch == ')')
            else:
                l -= (ch == ')')

        ans = []
        dfs(s, 0, l, r, ans)
        return ans
