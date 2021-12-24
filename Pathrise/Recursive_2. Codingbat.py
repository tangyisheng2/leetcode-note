#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Recursive_2. Codingbat.py
# @Time      :12/24/21 11:15 AM
# @Author    :Eason Tang

"""
Given a string s and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.
Examples:
substrDist("catcowcat", "cat") → 9
substrDist("catcowcat", "cow") → 3
substrDist("xcatcowcatxxx", "cat") → 9

"""


def substrDist(s, sub):
    n, m = len(s), len(sub)
    if m > n: return 0
    isAtStart = s[:m] == sub
    isAtEnd = s[n - m:] == sub
    if isAtStart and isAtEnd: return n  # The [0, n] situation is judged on here
    if isAtStart: return substrDist(s[:n - 1], sub)
    if isAtEnd: return substrDist(s[1:], sub)
    return substrDist(s[1: -1], sub)
    # The index must be [1, -1(=n - 1)] or we will get infinite loop


def substrDist2(s, sub):
    def rec(start, end):
        """
        This function finds the longest substring in s[start: end]
        """
        n, m = end - start, len(sub)
        if m > n:
            return 0  # basecase
        isAtStart = s[start: start + m] == sub
        isAtEnd = s[end - m: end] == sub
        if isAtStart and isAtEnd:
            return end - start
        if not isAtStart:
            start += 1
        if not isAtEnd:
            end -= 1
        return rec(start, end)

    return rec(0, len(s))

print(substrDist2("catcowcat", "cat"))
print(substrDist2("catcowcat", "cow"))
print(substrDist2("xcatcowcatxxx", "cat"))
