"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5)-> true
call isBadVersion(4)-> true
Then 4 is the first bad version.
Example 2:
Input: n = 1, bad = 1
Output: 1
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
def isBadVersion(version):
    return version >= 256
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        简单的二分法
        二分查找笔记：https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = (left + right) // 2
        while left < right:
            if not isBadVersion(mid - 1) and isBadVersion(mid):  # 判断出现第一个坏版本的依据是：前一个版本OK，但当前版本是坏版本
                return mid
            if isBadVersion(mid):  # 中间值坏
                right = mid - 1
                mid = (left + right) // 2
            else:
                left = mid + 1
                mid = (left + right) // 2
        return mid


test = Solution()
ret = test.firstBadVersion(256)
print(ret)
