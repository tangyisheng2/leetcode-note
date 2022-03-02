#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :20. Valid Parentheses.py
# @Time      :3/2/22
# @Author    :Eason Tang


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in {'(', '[', '{'}:
                stack.append(ch)
            elif ch in {')', ']', '}'}:
                if not stack:  # If the stack is empty, can not pair
                    return False

                left_parenthess = stack.pop()
                if pair[left_parenthess] != ch:  # If the parenthess if not paired
                    return False

        return not stack  # Check unpair left parenthess at the end
