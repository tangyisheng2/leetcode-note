#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :385. Mini Parser.py
# @Time      :4/14/22
# @Author    :Eason Tang


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

    def add(self, elem):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
        """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        index = 0

        def dfs():
            """
            This function returns the parse result of the integer
            """
            nonlocal index
            if s[index] == '[':
                """
                This is a nested integer and we need to parse it
                """
                index += 1
                next_ = NestedInteger()  # Initialize the next nestedList object
                while s[index] != ']':
                    next_.add(dfs())  # Construct the next nestedInteger
                    if s[index] == ',':  # If reach the end of current elem
                        index += 1
                index += 1
                return next_

            else:
                """
                This is just an integer and we just need to convert it to number
                """
                isNegative = False
                if s[index] == '-':
                    isNegative = True
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num *= 10
                    num += int(s[index])
                    index += 1
                if isNegative:
                    num = -num
                return NestedInteger(num)

        return dfs()  # !/usr/bin/env python


# -*- coding:utf-8 -*-
# @FileName  :385. Mini Parser.py
# @Time      :4/14/22
# @Author    :Eason Tang


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

    def add(self, elem):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
        """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        index = 0

        def dfs():
            """
            This function returns the parse result of the integer
            """
            nonlocal index
            if s[index] == '[':
                """
                This is a nested integer and we need to parse it
                """
                index += 1
                next_ = NestedInteger()  # Initialize the next nestedList object
                while s[index] != ']':  # For the all nestedInteger comming up, add then to the nestedInteger
                    next_.add(dfs())  # Construct the next nestedInteger
                    if s[index] == ',':  # If reach the end of current elem
                        index += 1
                next_.add(dfs())  # Construct the next nestedInteger
                index += 1
                return next_

            else:
                """
                This is just an integer and we just need to convert it to number
                """
                isNegative = False  # check if is negative
                if s[index] == '-':
                    isNegative = True
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    # Calculate the number
                    num *= 10
                    num += int(s[index])
                    index += 1
                if isNegative:
                    # Add '-' if the number is negative
                    num = -num
                return NestedInteger(num)

        return dfs()


test = Solution()
ret = test.deserialize("[123,[456,[789]]]")
