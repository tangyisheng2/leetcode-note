# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1239. Maximum Length of a Concatenated String with Unique Characters.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def validStr(string):
            """
            判断字符串中是否有重复数字
            :param string:
            :return:
            """
            return len(set(string)) == len(string)

        dp = []  # dp存储目前有效的字符串
        for s in arr:
            if not validStr(s):  # 如果s本身就有重复元素则直接跳过
                continue
            for s_ in list(dp):  # 对于dp中的所有元素尝试拼接
                if validStr(s_ + s):  # 如果拼接后是有效的结果
                    dp.append(s_ + s)  # 添加拼接后
            dp.append(s)  # 如果都没有小则直接添加arr中的元素作为一个单独的字符串
        return len(max(dp, key=len)) if dp else 0


if __name__ == '__main__':
    ret = Solution().maxLength(arr=["un", "iq", "ue"])
