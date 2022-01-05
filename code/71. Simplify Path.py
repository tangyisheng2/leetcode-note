#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :71. Simplify Path.py
# @Time      :1/5/22 2:29 PM
# @Author    :Eason Tang
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/') # We split the string path to a list
        stack = []
        for name in path_list:
            if not name:    # If the name is empty e.g. //
                continue
            if name == '.': # If the name is single dot that represents the current dict
                continue
            if name == '..' and stack:  # If the name is '..', return to the parent dict
                stack.pop()
                continue
            elif name == '..' and not stack:    # If the name is '..' but the stack is empty, do nothing
                continue
            stack.append(name)

        return '/' + '/'.join(stack)
