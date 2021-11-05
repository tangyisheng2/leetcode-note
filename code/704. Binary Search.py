"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-9999 <= nums[i], target <= 9999
All the integers in nums are unique.
nums is sorted in an ascending order.

"""
from typing import List

# class Solution:
#     def search(self, nums, target: int) -> int:
#         lo = 0
#         hi = len(nums) - 1
#         while hi >= lo:  # 慎重选择截截止条件，一般要循环到数组为空
#             mid = (lo + hi) // 2
#             if nums[mid] == target:  # 找到匹配，注意跳出条件要放在开始
#                 return mid
#             elif nums[mid] < target:  # 二分点数值小于target，二分点右移
#                 lo = mid + 1
#             if nums[mid] > target:  # 二分点数值大于target，二分点左移
#                 hi = mid - 1
#         return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                return mid

        return -1