#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :125. Valid Palindrome.py
# @Time      :2021/6/21 3:29 PM
# @Author    :Eason Tang


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum()) # Ignore Cases, space, and markings
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
