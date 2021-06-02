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
        def binarysearch(data, target):
            """
            二分法查找
            :param data:
            :param target:
            :return:
            """
            lower = 0
            upper = len(data) - 1
            mid = math.floor((lower + upper) * 0.5)
            found = False
            while lower <= upper:
                """
                进行二分查找
                注意用小于等于，当三个指针同时指向一个元素
                则找到了元素
                """
                if target < data[mid]:
                    upper = mid - 1
                    mid = math.floor((lower + upper) * 0.5)
                elif target > data[mid]:
                    lower = mid + 1
                    mid = math.floor((lower + upper) * 0.5)
                elif target == data[mid]:  # 有可能在移位之后存在相等的情况
                    return True, mid  # 在相等的情况下返回
            return found, mid  # 当移位之后仍然找不到匹配时返回

        first_row = []
        for i in range(len(matrix)):
            first_row.append(matrix[i][0])  # 添加第一行数据
        found, mid = binarysearch(first_row, target)  # 对每一行的第一列数据进行比较
        if found:
            return found
        else:
            found, _ = binarysearch(matrix[mid], target)  # 对该行剩下的数据进行比较
            return found


test = Solution()
print(test.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
                        , target=11))   # testcase
