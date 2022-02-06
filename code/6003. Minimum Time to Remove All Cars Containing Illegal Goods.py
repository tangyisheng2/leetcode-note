#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :6003. Minimum Time to Remove All Cars Containing Illegal Goods.py
# @Time      :2/5/22
# @Author    :Eason Tang
from typing import List, Optional


class Solution:
    def minimumTime(self, s: str) -> int:
        """
        DP + 前缀和 + 后缀和
        :param s:
        :return:
        """
        n = len(s)
        pre = [0 for _ in range(len(s) + 1)]
        suf = [0 for _ in range(len(s) + 1)]
        ans = float('inf')

        for i in range(1, n + 1):
            """
            前缀和
            1. 若当前字符 = '0', 则pre[i] = pre[i - 1]
            2. 若当前字符 = '1'，则pre[i] = min(pre[i - 1] + 2, i)
            有两种转移方法：只从左边按顺序删除花费为i；从中间直接删除花费为pre[i - 1] + 2
            """
            pre[i] = pre[i - 1] if s[i - 1] == '0' else min(pre[i - 1] + 2, i)

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] if s[i] == '0' else min(suf[i + 1] + 2, n - i)

        """
        切割分割点，找寻从前从后删除消费最低的组合
        """
        for i, j in zip(pre, suf):
            ans = min(ans, i + j)

        return ans

    def minimumTime2(self, s: str) -> int:
        """
        优化：
        1. 先计算suf，并且在美剧分割点的同时计算pre
        2. 由于pre转移的当前状态只和上一个状态有关，因此可以把pre数组优化成一个变量
        3. 当s[i]=0时，pre[i]和suf[i]军部变化，因此仅需要考虑s[i] = 1时pre[i] + suf[i + 1]的最小值
        :param s:
        :return:
        """
        n = len(s)
        # pre = [0 for _ in range(len(s) + 1)]
        pre = 0
        suf = [0 for _ in range(len(s) + 1)]

        # for i in range(1, n + 1):
        #     pre[i] = pre[i - 1] if s[i - 1] == '0' else min(pre[i - 1] + 2, i)

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] if s[i] == '0' else min(suf[i + 1] + 2, n - i)

        ans = suf[0]

        # for i, j in zip(pre, suf):
        #     ans = min(ans, i + j)

        for i, ch in enumerate(s):
            if ch == '1':
                pre = min(pre + 2, i + 1)
                ans = min(ans, pre + suf[i + 1])

        return ans


    def minimumTime3(self, s: str) -> int:
        """
        将suf上初中检测线给的花费合并到pre，这样suf敬畏删除后缀车厢的花费，则可以直接用下表进行计算。
        因此可以省略suf的计算流程并直接得出答案
        :param s:
        :return:
        """
        ans = n = len(s)
        pre = 0
        for i, ch in enumerate(s):
            if ch == '1':
                pre = min(pre + 2, i + 1)
            ans = min(ans, pre + n - 1 - i)
        return ans
