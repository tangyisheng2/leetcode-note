"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
import math


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        import numpy
        def binarysearch(data, target):
            lower = 0
            upper = len(data) - 1
            mid = math.floor((lower + upper) * 0.5)
            found = False
            if target == data[mid]: #如果一上来就找到了匹配
                found = True
                return found, lower, upper, mid
            while lower <= upper:
                if target < data[mid]:
                    upper = mid - 1
                    mid = math.floor((lower + upper) * 0.5)
                elif target > data[mid]:
                    lower = mid + 1
                    mid = math.floor((lower + upper) * 0.5)
                elif target == data[mid]: #有可能在移位之后存在相等的情况
                    found = True
                    return found, lower, upper, mid #在相等的情况下返回
            return found, lower, upper, mid #当移位之后仍然找不到匹配时返回

        found, lower_row, upper_row, mid = binarysearch(numpy.asarray(matrix)[:, 0], target)
        if found:
            return found
        else:
            found, _, _, _ = binarysearch(numpy.asarray(matrix)[mid, :], target)
            return found


test = Solution()
print(test.searchMatrix(matrix=[[1, 3]], target=3))
pass
