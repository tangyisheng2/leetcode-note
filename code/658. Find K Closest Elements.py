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


# class Solution:
#     def findClosestElements(self, arr: list, k: int, x: int) -> list:
#         """
#         思路：通过逐次移动左边以及右边的指针来逐渐逼近答案
#         :param arr: 数组
#         :param k: 区间长度
#         :param x: 目标
#         :return: 最靠近目标的k个数
#         """
#
#         res = arr
#         while len(res) > k:
#             if abs(res[0] - x) < abs(res[-1] - x) or \
#                     (abs(res[0] - x) == abs(res[-1] - x) and res[0] < res[-1]):  # 左边小，删除右边
#                 del res[-1]
#             else:
#                 del res[0]
#         return res
import collections


class Solution:
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        """
        思路：

        :param arr: 数组
        :param k: 区间长度
        :param x: 目标
        :return: 最靠近目标的k个数
        """
        lo = 0
        hi = len(arr) - 1
        mid = 0  # 先定义防止翻车
        while lo <= hi:  # 二分法查找稍比x大的元素
            mid = (lo + hi) // 2
            if arr[mid] == x:
                break
            if arr[mid - 1] < x <= arr[mid]:  # 需要注意的是，使用大于等于号。因为当x等于二分点元素的时候也能符合我们的条件
                break
            elif arr[mid] < x:
                lo = mid + 1
            elif arr[mid] > x:
                hi = mid - 1
        lo = mid - k if mid - k > 0 else 0  # 在确定了x的位置idx后，答案数组位于[idx-k, idx+k]的区间。这里要注意下标不要越界
        hi = mid + k if mid + k > len(arr) else len(arr)
        arr = arr[lo:hi + 1]  # 将区间外的元素删掉
        while len(arr) > k:  # 通过逐次移动左边以及右边的指针来逐渐逼近答案
            if abs(arr[0] - x) < abs(arr[-1] - x) or \
                    (abs(arr[0] - x) == abs(arr[-1] - x) and arr[0] < arr[-1]):  # 根据题目给出的判定条件判断
                del arr[-1]  # 左边小，删除右边
            else:
                del arr[0]
        return arr


test = Solution()
ret = test.findClosestElements([1], 1, 1)
print(ret)
