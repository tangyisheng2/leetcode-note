#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :784. Letter Case Permutation.py
# @Time      :10/19/21 10:45 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(s, idx, ans):
            if idx == len(s):
                ans.append("".join(s))
                return

            dfs(s, idx + 1, ans)    # Branch1： 只是往后移动一位，什么都不做
            if s[idx].isalpha():    # Branch2:  变更字母大小写
                s[idx] = s[idx].upper() if "a" <= s[idx] <= "z" else s[idx].lower()
                dfs(s, idx + 1, ans)
                s[idx] = s[idx].upper() if "a" <= s[idx] <= "z" else s[idx].lower()

        s = list(s)
        print(s)
        ans = []
        dfs(s, 0, ans)
        return ans

# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         ans = [[]]
#
#         for char in s:
#             n = len(ans)
#             if char.isalpha():  # 如果是字母
#                 for i in range(n):
#                     ans.append(ans[i].copy())  # 将ans复制两份
#                     ans[i].append(char.lower())  # 在第一份结果的背后加上小写的char
#                     ans[i + n].append(char.upper())  # 在第二份结果的背后加上大写的char
#             else:
#                 for i in range(n):
#                     ans[i].append(char)  # 数字就直接在所有结果的后面加上
#
#         return ["".join(i) for i in ans]


test = Solution()
res = test.letterCasePermutation(s="a1b2")
print(res)
