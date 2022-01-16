#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1220. Count Vowels Permutation.py
# @Time      :1/16/22
# @Author    :Eason Tang
from typing import List, Optional


# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         """
#         DFS超时
#         """
#         def dfs(current_state, remaining_cnt):
#             """
#             This function updates the answer using dfs
#             """
#             nonlocal ans
#             if remaining_cnt == 0:
#                 ans += 1
#                 return
#
#             for character in candidate:
#                 if not current_state:
#                     # If the current state is empty, then every character is valid
#                     current_state.append(character)
#                     dfs(current_state, remaining_cnt - 1)
#                     current_state.pop()
#                 else:
#                     # If the current state is not empty, we only append valid characters based on the rule
#                     if current_state[-1] == 'a' and character == 'e' or \
#                             current_state[-1] == 'e' and character in {'a', 'i'} or \
#                             current_state[-1] == 'i' and character != 'i' or \
#                             current_state[-1] == 'o' and character in {'i', 'u'} or \
#                             current_state[-1] == 'u' and character == 'a':
#                         current_state.append(character)
#                         dfs(current_state, remaining_cnt - 1)
#                         current_state.pop()
#
#         ans = 0
#         candidate = ['a', 'e', 'i', 'o', 'u']
#         dfs([], n)
#         return int(ans % (10e9 + 7))

# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         """
#         DP v1, 超时
#         """
#         dp = [[] for _ in range(n + 1)]
#         candidate = ['a', 'e', 'i', 'o', 'u']
#         dp[1] = candidate
#         for i in range(2, n + 1):
#             for word in dp[i - 1]:
#                 if word[-1] == 'a':
#                     dp[i].append(f'{word}e')
#                 elif word[-1] == 'e':
#                     dp[i].append(f'{word}a')
#                     dp[i].append(f'{word}i')
#                 elif word[-1] == 'i':
#                     dp[i].append(f'{word}a')
#                     dp[i].append(f'{word}e')
#                     dp[i].append(f'{word}o')
#                     dp[i].append(f'{word}u')
#                 elif word[-1] == 'o':
#                     dp[i].append(f'{word}i')
#                     dp[i].append(f'{word}u')
#                 elif word[-1] == 'u':
#                     dp[i].append(f'{word}a')
#
#         return int(len(dp[n]) % (10e9 + 7))

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        设dp[i][j]，其中i为元音长度，j为该长度下以第j个原因结尾的单词个数(元音: a, e, i, o, u)
        """
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007,
                  dp[2], (dp[2] + dp[3]) % 1000000007)
        return sum(dp) % 1000000007


test = Solution()
ret = test.countVowelPermutation(10)
