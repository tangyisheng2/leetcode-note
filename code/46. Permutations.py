# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   46. Permutations.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Base case:
        1. Only 1 element: return [[n]]
        2. Only 2 elements: swap the 2 element

        >= 3 elements: fix the first element the recuse the rest
        """

        def dfs(prefix, depth, max_depth, used):
            if depth == max_depth:  # basecase
                ans.append(prefix[:])
                # 在 Java 中，参数传递是 值传递，对象类型变量在传参的过程中，复制的是变量的地址。这些地址被添加到 res 变量，但实际上指向的是同一块内存地址，因此我们会看到 6
                # 个空的列表对象。解决的方法很简单，在 res.add(path); 这里做一次拷贝即可。
                # 链接：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

                return

            for i in range(len(nums)):
                if not used[i]:
                    # 递归
                    used[i] = True
                    prefix.append(nums[i])
                    dfs(prefix, depth + 1, max_depth, used)
                    # 复原
                    used[i] = False
                    prefix.pop()
            return ans

        ans = []
        used = [False for _ in range(len(nums))]
        return dfs([], 0, len(nums), used)


# New Version
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, used, current_state, ans):
            if len(current_state) == len(nums):
                ans.append(current_state[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_state.append(nums[i])
                    dfs(nums, used, current_state, ans)
                    current_state.pop()
                    used[i] = False

        ans = []
        used = [False for _ in range(len(nums))]
        dfs(nums, used, [], ans)
        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.permute([1, 2, 3]))
