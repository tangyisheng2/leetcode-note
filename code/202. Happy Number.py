#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :202. Happy Number.py
# @Time      :5/28/22
# @Author    :Eason Tang


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Get the digits
        """

        def getDigits(num):
            if num < 0:
                return -1

            if num < 10:
                return [num]

            ans = []
            while num > 0:
                digit = num % 10
                num //= 10
                ans.append(digit)

            return ans[::-1]

        visited = set()
        while n > 1:
            # If the number is visited (loop detected), return false
            if n in visited:
                return False
            # Add the current visited set
            visited.add(n)
            digitArr = getDigits(n)
            # Generate next num
            n = sum([digit ** 2 for digit in digitArr])
        return True

        # Time: O(logn) -> Mainly caused by getting digits
        # Time: O(logn + n??)

    def isHappy2(self, n: int) -> bool:
        def getNext(num):
            if num < 0:
                return -1

            if num < 10:
                return num ** 2

            ans = 0
            while num > 0:
                digit = num % 10
                num //= 10
                ans += digit ** 2

            return ans

        slow = n
        fast = getNext(n)

        while fast != 1 and slow != fast:
            # 如果n是一个快乐数，则快指针将首先到达1
            # 如果n不是一个快乐数，则
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1
