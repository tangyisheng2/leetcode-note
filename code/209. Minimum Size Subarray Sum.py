"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no
such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

# class Solution:
#     def minSubArrayLen(self, target: int, nums: list) -> int:
#         """
#         暴力解法
#         :param target:
#         :param nums:
#         :return:
#         """
#         if sum(nums) < target:
#             return 0
#         res = len(nums)
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if sum(nums[i:j + 1]) >= target:
#                     res = min(res, j - i + 1)
#                     break
#         return res
import collections


class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        """
        双指针解法
        Reference Solution:
        https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/javade-jie-fa-ji-bai-liao-9985de-yong-hu-by-sdwwld/
        https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/monkti-jie-yong-zui-shao-de-yu-yan-he-da-txe4/
        :rtype: object
        :param target:
        :param nums:
        :return:
        """
        lo = 0  # 左指针开始为0
        cur_sum = 0  # 和初始值为0
        res = len(nums) + 1  # res初始值为数组长度+1，子数组长度最多也不会超过数组长度
        for hi in range(len(nums)):  # 队列头指针
            cur_sum += nums[hi]  # 计算当前子序列的长度
            while cur_sum >= target:  # 如果当前子序列的和超过了target
                res = min(res, hi - lo + 1)  # 更新最小子序列长度，+1是由于数组index从0开始
                cur_sum -= nums[lo]  # 队尾元素出栈，更新当前子序列的和
                lo += 1  # 队尾右移
        return res if res != len(nums) + 1 else 0


test = Solution()
ret = test.minSubArrayLen(15, [1, 2, 3, 4, 5])
print(ret)
