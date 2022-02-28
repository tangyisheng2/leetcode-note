#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1601. Maximum Number of Achievable Transfer Requests.py
# @Time      :2/27/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for mask in range(1 << len(requests)):  # 创建所有的二进制自负
            cnt = mask.bit_count()  # 计算二进制表现中一的个数中非0字符串的个数
            if cnt <= ans:  # 如果当前选择方案小于最大的答案，提前剪枝
                continue
            delta = [0] * n  # 记录每个公司的流入流出差
            for i, (x, y) in enumerate(requests):  # 遍历每一个requests
                if mask & (1 << i):  # 如果选择当前方案（二进制位 == 1）
                    delta[x] += 1
                    delta[y] -= 1
            if all(x == 0 for x in delta):  # 判断是否所有的楼层都delta == 0，如果是则为合法方案
                ans = cnt
        return ans

    def maximumRequests2(self, n: int, requests: List[List[int]]) -> int:
        delta = [0] * n
        ans, cnt, zero = 0, 0, n

        # zero是delta中0元素的树木

        def dfs(pos: int) -> None:
            nonlocal ans, cnt, zero
            if pos == len(requests):
                if zero == n:  # 如果选择到当前是合法的状态
                    ans = max(ans, cnt)
                return

            # 不选 requests[pos]
            dfs(pos + 1)

            # 选 requests[pos]
            # -----保存状态-----
            z = zero  # 保存当前zero的状态
            cnt += 1  # 换楼请求 + 1
            # -----进行DFS-----
            x, y = requests[pos]
            zero -= delta[x] == 0  # 如果delta[x] == 0，则改变后delta[x]不再为0，此时我们更新zero的值
            delta[x] -= 1  # 更新delta[x]
            zero += delta[x] == 0  # 如果delta[x]更新后 == 0，则zero += 1

            zero -= delta[y] == 0  # 如果delta[y] == 0，则改变后delta[y]不再为0，此时我们更新zero的值
            delta[y] += 1  # 更新delta[y]
            zero += delta[y] == 0

            dfs(pos + 1)  # 进行dfs
            # -----还原状态-----
            delta[y] -= 1
            delta[x] += 1
            cnt -= 1  # 换楼请求 - 1
            zero = z  # 还原zero状态

        dfs(0)
        return ans
