#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :3. Longest Substring Without Repeating Characters.py
# @Time      :10/8/21 3:53 PM
# @Author    :Eason Tang
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         occured = set()  # 已经出现的字母的集合
#         r = 0
#         max_count = 0
#
#         for i in range(n):  # 数组每次右移都删除左边的字母
#             if i != 0:  # 当数组刚开始的时候，集合总并没有数组可以做删除
#                 occured.remove(s[i - 1])
#             while r < n and s[r] not in occured:
#                 # 向右移动直到出现第一个重复的字母，则得到从第i个下表开始的Longest Substring Without
#                 # Repeating Characters
#                 occured.add(s[r])
#                 r += 1
#             max_count = max(max_count, r - i)
#         return max_count


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = -1  # 右指针刚刚初始化时候需要设置成-1，避免"p"情况下计算出错
        res = 0
        c_dict = {} # 已经出现的次数
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > r:
                """
                字母c已经出现过了，那么在下一次出现同样的字母c的时候说明当前最大不重复的字串已经结束
                所以我们可以直接把左指针移到重复字母出现的位置，并且更新记录最后字母出现的最后的idx的hash
                """
                r = c_dict[c]
                c_dict[c] = i
            else:
                """
                如果是没有出现的字母，我们把它记录到hashmap，并且更新最大的字串长度
                """
                c_dict[c] = i
                res = max(res, i-r)
        return res

test = Solution()
print(test.lengthOfLongestSubstring(s="p"))
