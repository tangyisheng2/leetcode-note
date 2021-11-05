#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :93. Restore IP Addresses.py
# @Time      :11/1/21 11:29 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # 判断数组中的数字是否合法
        def isValid(p):
            if p == '0':
                return True  # 解决"0000"
            if p[0] == '0':
                return False
            if 0 < int(p) < 256:
                return True
            return False

        def backtrack(s, startIndex, path, res):
            """
            :param s:
            :param startIndex:
            :param path:
            :param res:
            :return:
            """
            if len(s) > 12:
                return  # 字符串长度最大为12
            if len(path) == 4 and startIndex == len(s):  # 确保切割完，且切割后的长度为4
                res.append(".".join(path[:]))  # 字符拼接
                return

            for i in range(startIndex, len(s)):
                if len(s) - startIndex > 3 * (4 - len(path)):
                    # s - start的下标 > 3 * (总段数 - 已切段个数）
                    continue  # 剪枝，剩下的字符串大于允许的最大长度则跳过
                p = s[startIndex:i + 1]  # 分割字符
                if isValid(p):  # 判断字符是否有效
                    path.append(p)
                else:
                    continue
                backtrack(s, i + 1, path, res)  # 寻找i+1为起始位置的子串
                path.pop()

        backtrack(s, 0, [], res)
        return res


test = Solution()
ret = test.restoreIpAddresses("25525511135")
print(ret)