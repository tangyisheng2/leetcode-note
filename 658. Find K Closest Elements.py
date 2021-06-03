"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""


# class Solution:
#     def findClosestElements(self, arr: list, k: int, x: int) -> list:
#         """
#         思路：通过逐次移动左边以及右边的指针来逐渐逼近答案
#         :param arr: 数组
#         :param k: 区间长度
#         :param x: 目标
#         :return: 最靠近目标的k个数
#         """
#         from math import fabs
#         left_idx = 0
#         right_idx = len(arr) - 1
#         if k >= len(arr):  # 如果目标区间本身比数组区间长
#             return arr  # 直接返回整个数组
#         while right_idx - left_idx >= k:
#             if (fabs(arr[left_idx] - x) < fabs(arr[right_idx] - x)) or \
#                     (fabs(arr[left_idx] - x) == fabs(arr[right_idx] - x) and left_idx < right_idx):
#                 # 左边元素差值较小，左边指针右移
#                 right_idx -= 1
#             # elif fabs(arr[left_idx] - x) == fabs(arr[right_idx] - x) and left_idx < right_idx:
#             #     left_idx += 1
#             else:
#                 # 左边元素差值较小，右边指针左移
#                 left_idx += 1
#         return arr[left_idx:right_idx + 1]  # 注意这里取的是闭区间，所以右边界要+1


class Solution:
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        """
        思路：通过逐次移动左边以及右边的指针来逐渐逼近答案
        :param arr: 数组
        :param k: 区间长度
        :param x: 目标
        :return: 最靠近目标的k个数
        """

        res = arr
        while len(res) > k:
            if abs(res[0] - x) < abs(res[-1] - x) or \
                    (abs(res[0] - x) == abs(res[-1] - x) and res[0] < res[-1]):  # 左边小，删除右边
                del res[-1]
            else:
                del res[0]
        return res


test = Solution()
ret = test.findClosestElements([1, 2, 3, 4, 5], 4, 3)
print(ret)
