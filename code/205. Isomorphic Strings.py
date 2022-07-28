#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :205. Isomorphic Strings.py
# @Time      :7/27/22
# @Author    :Eason Tang


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        if len(s) != len(t):
            return False

        st_mapping = {}
        ts_mapping = {}

        for i in range(len(s)):
            if s[i] not in st_mapping:  # Update mapping
                st_mapping[s[i]] = t[i]
            elif s[i] in st_mapping and st_mapping[s[i]] != t[i]:  # Check if there is only one mapping
                return False

            if t[i] not in ts_mapping:
                ts_mapping[t[i]] = s[i]
            elif t[i] in ts_mapping and ts_mapping[t[i]] != s[i]:
                return False

        return True
