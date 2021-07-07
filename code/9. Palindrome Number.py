# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   9. Palindrome Number.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or \
                (x > 0 and x % 10 == 0):
            # 存在负号，一定不是回文
            # 同时对于大于0的数，因为最高位不能为0
            return False

        x_rev = 0
        while x > x_rev:
            x_rev = x_rev * 10 + x % 10
            x //= 10    # 注意这里需要整除

        return x == x_rev or x == x_rev // 10


test = Solution()
test.isPalindrome(11)
