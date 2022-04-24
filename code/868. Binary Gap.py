#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :868. Binary Gap.py
# @Time      :4/24/22
# @Author    :Eason Tang
class Solution:
    def binaryGap(self, n: int) -> int:
        last_1_idx, ans, cur_idx = -1, 0, 0
        while n:
            if n & 1:  # 如果n二进制的最后一位是1
                if last_1_idx != -1:  # 并且上一个1的位置不为-1的话
                    ans = max(ans, cur_idx - last_1_idx)  # 更新答案
                last_1_idx = cur_idx
            n >>= 1  # n二进制向右移动一位
            cur_idx += 1  # 目前指针+1
        return ans
