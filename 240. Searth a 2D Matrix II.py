"""
240. Search a 2D Matrix II
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""


class Solution:
    def searchMatrix(self, matrix, target: int):
        """
        搜索矩阵
        仔细观察矩阵可以发现：
        右边的元素永远比左边的大
        下面的元素永远比上面的大
        因此可以从对角线入手，逐次移动指针
        Reference Solution: https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/
        :param matrix:
        :param target:
        :return:
        """
        row = len(matrix) - 1  # 初始指针放在左下角
        col = 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:  # 找到target
                return True
            elif matrix[row][col] < target:  # 目前数字比target小，向右移动
                col += 1
            else:  # 目前数字比target大，向上移动
                row -= 1
        return False  # Default Case


test = Solution()
res = test.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=5)
print(res)
