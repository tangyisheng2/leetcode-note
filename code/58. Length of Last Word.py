#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :58. Length of Last Word.py
# @Time      :1/1/22 12:10 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip().lstrip()
        s = s.split(" ")[-1]
        return len(s)
