"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""


class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if not nums:  # 如果数组不存在
            return 0
        dp = [1 for _ in range(len(nums))]  # dp初始化，在初始状态下没有最长子链所以dp=1
        for i in range(len(nums)):  # 遍历所有元素
            for j in range(i):
                """
                对nums[j]来说，nums[i]能链接在nums[j]后面的条件为
                nums[i] < nums[j]
                因此比较nums[j]的大小，如果nums[j] < nums[i]
                这dp[i] = dp[j] + 1
                """
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    """
                    1.  如果nums[1]和nums[0]能组成增长子串
                        并且nums[5]和nums[1]能组成增长子串，
                        那么明显有nums[0]-nums[1]-nums[5]这条增长子串
                    2.  例如在nums[5]中需要于nums[0]-nums[4]进行对比
                        nums[5] > nums[0]，因此dp[5] = dp[0] + 1 = 2
                        nums[5] > nums[1]，因此dp[5] = dp[1] + 1 = 3
                        nums[5] < nums[2]，跳过
                        nums[5] < nums[3]，跳过
                        nums[5] < nums[4]，跳过
                    3.  在逐步遍历中找到dp的最大子串
                        上面要用max的原因是因为nums[i - 1]所可以组成的子串不一定是长度最长的
                        因此我们使用max函数来确保nums[i]接到了最长的子串三
                    """
        return max(dp)


test = Solution()
print(test.lengthOfLIS((
    [1, 3, 6, 7, 9, 4, 10, 5, 6])))
