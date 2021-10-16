#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :567. Permutation in String.py
# @Time      :10/15/21 11:44 PM
# @Author    :Eason Tang

# Brute Force
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         def permutation(str, path, used, depth, ans):
#
#             if depth == len(s1):
#                 ans.append(path)
#                 return
#
#             for i in range(len(used)):
#                 if not used[i]:
#                     used[i] = True
#                     permutation(str, f'{path}{s1[i]}', used, depth + 1, ans)
#                     used[i] = False
#             return ans
#
#         permute_str = permutation("ab", "", [False for _ in range(len(s1))], 0, [])
#         for s1_str in permute_str:
#             if s1_str in s2:
#                 return True
#         return False
#
#
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         """
#         Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#         s2 contains a permutation of s1 -> 说明我们建立一个长度为s1的滑动窗口并对其进行遍历即可
#         """
#         # https://leetcode-cn.com/problems/permutation-in-string/solution/zhu-shi-chao-xiang-xi-de-hua-dong-chuang-rc7d/
#         import collections
#         n = len(s1)  # s1是滑动窗口长度
#         hash_s1 = collections.Counter(s1)
#
#         for i in range(len(s2) - n + 1):
#             hash_s2 = collections.Counter(s2[i:i + n])
#             if hash_s1 == hash_s2:
#                 return True
#
#         return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
        s2 contains a permutation of s1 -> 说明我们建立一个长度为s1的滑动窗口并对其进行遍历即可
        """
        # https://leetcode-cn.com/problems/permutation-in-string/solution/zhu-shi-chao-xiang-xi-de-hua-dong-chuang-rc7d/
        import collections
        n = len(s1)  # s1是滑动窗口长度
        hash_s1 = collections.Counter(s1)
        hash_s2 = collections.Counter(s2[:n])
        if hash_s1 == hash_s2:
            return True
        for i in range(n, len(s2)):
            # 删除左边元素
            # 增加右边元素
            # 判断是否想等
            hash_s2[s2[i - n]] -= 1
            if hash_s2[s2[i - n]] == 0:
                hash_s2.pop(s2[i - n])
            hash_s2[s2[i]] += 1
            if hash_s1 == hash_s2:
                return True

        return False


test = Solution()
test.checkInclusion("adc", "dcda")
