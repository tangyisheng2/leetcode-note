# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   14. Longest Common Prefix.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List
# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         Python特性
#         :type strs: List[str]
#         :rtype: str
#         """
#         res = ""
#         for tmp in zip(*strs):
#             tmp_set = set(tmp)
#             if len(tmp_set) == 1:
#                 res += tmp[0]
#             else:
#                 break
#         return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        https://leetcode-cn.com/problems/longest-common-prefix/solution/hua-jie-suan-fa-14-zui-chang-gong-gong-qian-zhui-b/
        :param strs:
        :return:
        """
        res = strs[0]
        for s in strs:
            if s == "":  # 当出现任意一个空串，结果都一定是空串
                return ""
            ptr = 0
            while s[ptr] == res[ptr] and ptr < min(len(s), len(res)):
                ptr += 1
            res = res[:ptr]
        return res


test = Solution()
test.longestCommonPrefix(["a"])

# ["flower","flow","flight"]
# ["dog","racecar","car"]
# ["","racecar","car"]
# ["ab", "a"]
