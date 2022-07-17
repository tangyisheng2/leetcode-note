#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :38. Count and Say.py
# @Time      :7/16/22
# @Author    :Eason Tang


class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(1, n):  # iterate through different n
            curr_ans = ""
            pos = 0
            start = 0

            while pos < len(ans):  # iterate through the string to say()
                # merge same number with f'{count}{number}'
                while pos < len(ans) and ans[pos] == ans[start]:
                    pos += 1
                # add the say string to current answer
                curr_ans += str(pos - start) + ans[start]
                # update the start for next iterate
                start = pos
            # update answer
            ans = curr_ans
        return ans


class Solution2:
    def countAndSay(self, n: int) -> str:
        def describe(s):
            """
            This function describes a string and returns a new one
            eg. 3322251 -> 23321511
            """
            ans = ""
            start = 0
            cur_idx = 0
            while cur_idx < len(s):
                while cur_idx < len(s) and s[cur_idx] == s[start]:
                    cur_idx += 1
                cnt = cur_idx - start
                ans += str(cnt) + s[start]
                start = cur_idx
            return ans

        if n == 1:
            return '1'  # Here it returns a string in base case, so we will always return a string
        else:
            return describe(self.countAndSay(n - 1))
