#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :680. Valid Palindrome II.py
# @Time      :2021/6/21 3:01 PM
# @Author    :Eason Tang

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        在允许最多删除一个字符的情况下，同样可以使用双指针，通过贪心算法实现。初始化两个指针 low 和 high
        分别指向字符串的第一个字符和最后一个字符。每次判断两个指针指向的字符是否相同，如果相同，则更新指针，
        令 low = low + 1 和 high = high - 1，然后判断更新后的指针范围内的子串是否是回文字符串。
        如果两个指针指向的字符不同，则两个字符中必须有一个被删除，此时我们就分成两种情况：即删除左指针对应的字符，
        留下子串 s[low + 1], s[low + 1], ..., s[high]，或者删除右指针对应的字符，
        留下子串 s[low], s[low + 1], ..., s[high - 1]。当这两个子串中至少有一个是回文串时，就说明原始字符串删除一个字符之后就以成为回文串。
        https://leetcode-cn.com/problems/valid-palindrome-ii/solution/cong-liang-ce-xiang-zhong-jian-zhao-dao-bu-deng-de/
        """

        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                # 由于[0, low], [high, len(s) - 1]已经是回文，因此不再判断
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True


test = Solution()
ret = test.validPalindrome("abc")
print(ret)
