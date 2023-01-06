from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Q: find the longest consecutive array that sums to (total - nums)
        Array representation: [left, right) *key point, always use [left, right)*
        init value:
        left = -1, right = 0 -> deduct the whole array
        Ends when left == n - 1 or right == n
        """
        n = len(nums)
        total = sum(nums)

        target = total - x
        cur_sum = 0

        right = 0

        ans = -1

        if target < 0:
            return -1

        if target == 0:
            return n

        for left in range(n):
            while right < n and cur_sum < target:
                cur_sum += nums[right]
                right += 1

            if cur_sum == target:
                ans = max(ans, right - left)
                print(left, right, cur_sum)

            if left > -1:
                cur_sum -= nums[left]

        return -1 if ans == -1 else n - ans
