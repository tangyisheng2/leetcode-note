# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   13. Roman to Integer.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        https://leetcode-cn.com/problems/roman-to-integer/solution/luo-ma-shu-zi-zhuan-zheng-shu-by-leetcod-w55p/
        通常情况下，罗马数字中小的数字在大的数字的右边。若输入的字符串满足该情况，
        那么可以将每个字符视作一个单独的值，累加每个字符对应的数值即可。
        若存在小的数字在大的数字的左边的情况，根据规则需要减去小的数字。
        对于这种情况，我们也可以将每个字符视作一个单独的值，若一个数字右侧的数字比它大，则将该数字的符号取反。
        XIV -> X - I + V = 10 - 1 + 5 = 14
        """
        res = 0
        symbol_table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i, ch in enumerate(s):
            val = symbol_table[ch]
            if i < len(s) - 1 and val < symbol_table[s[i + 1]]:
                res -= val
            else:
                res += val
        return res
