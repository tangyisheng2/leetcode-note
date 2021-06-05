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


# class Solution:
#     def searchMatrix(self, matrix, target: int):
#         """
#         搜索矩阵
#         仔细观察矩阵可以发现：
#         右边的元素永远比左边的大
#         下面的元素永远比上面的大
#         因此可以从对角线入手，逐次移动指针
#         Reference Solution: https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/
#         :param matrix:
#         :param target:
#         :return:
#         """
#         row = len(matrix) - 1  # 初始指针放在左下角
#         col = 0
#         while row >= 0 and col < len(matrix[0]):
#             if matrix[row][col] == target:  # 找到target
#                 return True
#             elif matrix[row][col] < target:  # 目前数字比target小，向右移动
#                 col += 1
#             else:  # 目前数字比target大，向上移动
#                 row -= 1
#         return False  # Default Case


# class Solution:
#     def searchMatrix(self, matrix, target: int):
#         """
#         二分查找法
#         通过对每一行与每一列分别进行二分查找获得结果
#         :param matrix:
#         :param target:
#         :return:
#         """
#
#         def binarysearch(matrix, target, start_idx, search_verticle):
#             lo = start_idx
#             hi = len(matrix) - 1 if not search_verticle else len(matrix[0]) - 1
#
#             while lo <= hi:
#                 mid = (lo + hi) // 2
#                 if not search_verticle:
#                     if matrix[mid][start_idx] < target:
#                         lo = mid + 1
#                     elif matrix[mid][start_idx] > target:
#                         hi = mid - 1
#                     elif matrix[mid][start_idx] == target:
#                         return True
#                 elif search_verticle:
#                     if matrix[start_idx][mid] < target:
#                         lo = mid + 1
#                     elif matrix[start_idx][mid] > target:
#                         hi = mid - 1
#                     elif matrix[start_idx][mid] == target:
#                         return True
#             return False
#
#         if not matrix:  # 如果Matrix不存在
#             return False
#         found = False
#         for i in range(min(len(matrix), len(matrix[0]))):
#             found_hor = binarysearch(matrix, target, i, False)
#             found_vec = binarysearch(matrix, target, i, True)
#             if found_vec or found_hor:
#                 found = True
#         return found

class Solution:
    def searchMatrix(self, matrix, target: int):
        """
        二分查找法v2
        通过对每一行与每一列分别进行二分查找获得结果
        相比v1又花了代码
        :param matrix:
        :param target:
        :return:
        """

        def binarysearch(data, target):
            """
            正常的二分查找
            :param data: 数据
            :param target: 目标
            :return: 是否找到
            """
            lo = 0
            hi = len(data) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if data[mid] == target:
                    return True
                if data[mid] < target:
                    lo = mid + 1
                elif data[mid] > target:
                    hi = mid - 1

            return False

        if not matrix:  # 如果Matrix不存在
            return False
        found = False
        # for i in range(len(matrix)):
        #     found_hor = binarysearch(matrix[i], target)
        #     if found_hor:
        #         found = True
        # for i in range(len(matrix[0])):
        #     found_vec = binarysearch([matrix[x][i] for x in range(len(matrix))], target)
        #     if found_vec:
        #         found = True
        for i in range(min(len(matrix), len(matrix[0]))):  # 事实上只需要搜索较短的一条边即可遍历所有的数据
            found_hor = binarysearch(matrix[i], target)  # 搜索行（固定行下标）
            found_vec = binarysearch([matrix[x][i] for x in range(len(matrix))], target)  # 搜索列，固定列下标
            if found_hor or found_vec:
                found = True

        return found


test = Solution()
res = test.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=5)
print(res)
