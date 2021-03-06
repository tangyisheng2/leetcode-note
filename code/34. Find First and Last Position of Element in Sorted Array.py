"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
from typing import List


# class Solution:
#     def searchRange(self, nums, target: int):
#         def search(mid, target):
#             """
#             考虑到nums中存在重复出现的数字，所以当nums[mid]找到target之后要向前向后搜索范围
#             :param mid: 中间index
#             :param target: 搜索目标
#             :return: [目标lower索引，目标upper索引]
#             """
#             ret_mid = mid  # 临时变量用于后续自增自减
#             while ret_mid > 0 and nums[ret_mid - 1] == target:
#                 """
#                 先向序列小的位置搜索
#                 需要注意当index为-1时已经越界但是并不会报错，所以要同时判断ret_mid > 0
#                 注意ret_mid等于0时不可取，这是因为下面ret_mid -= 1时将越界
#                 """
#                 ret_mid -= 1  # 向前移位
#             ret_low = ret_mid  # 找到low索引
#             ret_mid = mid  # 准备寻找upper索引
#             while ret_mid + 1 < len(nums) and nums[ret_mid + 1] == target:
#                 """
#                 同样要注意nums数组的下标有无越界，所以要判断ret_mid < len(nums) - 1
#                 """
#                 ret_mid += 1
#             ret_upper = ret_mid
#
#             return ret_low, ret_upper
#
#         low = 0
#         upper = len(nums) - 1
#         mid = math.ceil((upper + low) * 0.5)
#         if not nums:  # 判断空数组情况
#             return [-1, -1]
#         if target == nums[mid]:  # 判断刚开始已经找到匹配
#             return search(mid, target)
#         while low <= upper:
#             if target == nums[mid]:  # 判断mid下标是否已经找到target
#                 return search(mid, target)  # 搜索target的lower和upper下标
#             elif target < nums[mid]:  # 如果target比二分中间值小
#                 upper = mid - 1  # upper下移到中间值-1
#                 mid = math.ceil((upper + low) * 0.5)  # 重新计算中间值下标
#             elif target > nums[mid]:
#                 low = mid + 1
#                 mid = math.ceil((upper + low) * 0.5)
#         return [-1, -1]  # 搜索失败

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         def binarysearch(nums, target):
#             lo = 0
#             hi = len(nums) - 1
#             while lo <= hi:
#                 mid = (lo + hi) // 2
#                 if nums[mid] > target:
#                     hi = mid - 1
#                 elif nums[mid] < target:
#                     lo = mid + 1
#                 else:
#                     return mid
#             return -1
#
#         idx = binarysearch(nums, target)
#         if idx == -1:
#             return [-1, -1]
#         ptr_lo, ptr_hi = idx, idx
#         while ptr_lo > 0 and nums[ptr_lo - 1] == target:
#             ptr_lo -= 1
#         while ptr_hi < len(nums) - 1 and nums[ptr_hi + 1] == target:
#             ptr_hi += 1
#         return [ptr_lo, ptr_hi]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_lower():
            lo = 0
            hi = len(nums) - 1

            while lo < hi:
                mid = (lo + hi) // 2  # 当只有两个元素的时候，我们取下边界（因为我们找的是下边界
                if nums[mid] >= target:
                    hi = mid
                elif nums[mid] < target:  # nums[mid] <= target, since we need to lower boundary, move left
                    lo = mid + 1

                # if nums[mid] < target:
                #     lo = mid + 1
                # else:
                #     hi = mid

                # elif nums[mid] == target:
                #     hi = mid - 1

            if nums[lo] == target:
                return lo
            return -1

        def find_upper():
            lo = 0
            hi = len(nums) - 1

            while lo < hi:
                mid = (lo + hi + 1) // 2
                if nums[mid] <= target:
                    lo = mid
                else:
                    hi = mid - 1

            if nums[lo] == target:
                return lo
            return -1

        lower = find_lower()
        upper = find_upper()

        if 0 < lower <= upper < len(nums):
            return [lower, upper]
        return [-1, -1]


test = Solution()
ret = test.searchRange([5, 7, 7, 8, 8, 10], 6)
print(ret)
pass
