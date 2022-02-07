#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1405. Longest Happy String.py
# @Time      :2/6/22
# @Author    :Eason Tang
from typing import List, Optional


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        题目要求找到最长的快乐字符串，且快乐字符串中不含有三个连续相同的字母。为了找到最长的字符串，我们可以使用如下贪心策略：
        - 尽可能优先使用当前数量最多的字母，因为最后同一种字母剩余的越多，越容易出现字母连续相同的情况。如果构建完成最长的快乐字符串后还存
        在剩余未选择的字母，则剩余的字母一定为同一种字母且该字母的总数量最多。
        - 依次从当前数量最多的字母开始尝试，如果发现加入当前字母会导致出现三个连续相同字母，则跳过当前字母，直到我们找到可以添加的字母为止。
        实际上每次只会在数量最多和次多的字母中选择一个。
        - 如果尝试所有的字母都无法添加，则直接退出，此时构成的字符串即为最长的快乐字符串。
        :param a:
        :param b:
        :param c:
        :return:
        """
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])  # 对cnt的个数进行倒序排序
            hasNext = False  # 还可以接下一个字符串
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:  # 如果当前字符的剩余个数 <= 0，则不能继续使用这个数字插入
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:  # 如果当前结果个数大于2，且倒数两个数都与要添加的字符相同
                    continue
                hasNext = True  # 有下一个字符（当前的字符串合法）
                ans.append(ch)  # 添加字符串
                cnt[i][0] -= 1  # 更新cnt
                break
            if not hasNext:
                return ''.join(ans)
