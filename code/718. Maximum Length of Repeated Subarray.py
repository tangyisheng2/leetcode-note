"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

"""


# class Solution:
#     def findLength(self, nums1, nums2):
#         """
#         暴力枚举
#         :param nums1: integer array 1
#         :param nums2: integer array 2
#         :return: maximum length of a subarray that appears in both arrays.
#         """
#         if nums1 == nums2:
#             return len(nums1)
#         max_len = 0
#         for num1_index in range(len(nums1)):
#             for num2_index in range(len(nums2)):
#                 count = 0
#                 num1_index_tmp = num1_index # 枚举时的临时变量
#                 num2_index_tmp = num2_index
#                 while nums1[num1_index_tmp] == nums2[num2_index_tmp]:   # 从第一个开始相同的数字钱枚举
#                     num1_index_tmp += 1 # index后移
#                     num2_index_tmp += 1
#                     count += 1
#                     if not (num1_index_tmp < len(nums1) and num2_index_tmp < len(nums2)):  # 检测下标越界
#                         break
#                 max_len = max(max_len, count)
#         return max_len

class Solution:
    def findLength(self, nums1, nums2):
        """
        memorize function
        :param nums1:
        :param nums2:
        :return:
        """
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]  # 构建memo
        ans = 0
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                # dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    """
                    dp[i][j]存储了从当前index开始连续的最长子序列的长度
                    当nums[i + 1][j + 1]相等，且nums[i][j]相等时
                    最长子序列长度dp[i][j] = dp[i + 1][j + 1] + 1 
                    """
                else:
                    """
                    当nums[i + 1][j + 1]不相等，连续的最长子序列断开，所以长度为0
                    """
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans



test = Solution()
print(test.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
