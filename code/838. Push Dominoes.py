#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :838. Push Dominoes.py
# @Time      :2/20/22
# @Author    :Eason Tang


# class Solution:
#     def pushDominoes(self, dominoes: str) -> str:
#         import collections
#         n = len(dominoes)
#         q = collections.deque()
#         time = [-1] * n
#         force = [[] for _ in range(n)]
#         for i, f in enumerate(dominoes):
#             if f != '.':
#                 q.append(i)
#                 time[i] = 0
#                 force[i].append(f)
#
#         res = ['.'] * n
#         while q:
#             i = q.popleft()
#             if len(force[i]) == 1:  # 如果当前节点只受到一边的力，则会倒下；在不受力和
#                 res[i] = f = force[i][0]  # 当前节点的答案是当前受到力度的方向
#                 ni = i - 1 if f == 'L' else i + 1  # 下一个受到影响的节点
#                 if 0 <= ni < n:  # 如果节点没有越界
#                     t = time[i]  # i节点倒下的时间
#                     if time[ni] == -1:  # 当前节点名字为-1说明没有受到力
#                         q.append(ni)
#                         time[ni] = t + 1  # 下一个节点倒下的时间为t + 1
#                         force[ni].append(f)  # 当前节点倒下的受力方向与上一节点相同
#                     elif time[ni] == t + 1:
#                     # else:
#                         # 如果当前节点的时间为t + 1，已经访问过
#                         # 同时在此只有t + 1时候才能将当前force加入，不然骨牌已经倒了
#                         force[ni].append(f)  # 只添加受力
#         return ''.join(res)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        import collections
        n = len(dominoes)
        time = [-1] * n
        force_dir = [[] for _ in range(n)]
        ans = ['.'] * n

        q = collections.deque()
        for i, dominoe in enumerate(dominoes):
            if dominoe != '.':
                q.append(i)
                time[i] = 0
                force_dir[i].append(dominoe)

        while q:
            i = q.popleft()
            if len(force_dir[i]) == 1:  # 如果多米诺骨牌只受到一个力的作用，则才会倒下，否则两边同时受力则会直立
                ans[i] = force_dir[i][0]

                next_i = i + 1 if force_dir[i][0] == "R" else i - 1  # 计算下一个倒下的坐标
                if 0 <= next_i < n:  # 如果下一个的坐标没有越界
                    if time[next_i] == -1:  # 节点没被访问的话，可以直接访问
                        q.append(next_i)  # 将下一个节点入栈
                        time[next_i] = time[i] + 1  # 更新下一个节点时间
                        force_dir[next_i].append(force_dir[i][0])  # 更新下一个节点的受力
                    elif time[next_i] == time[i] + 1:  # 当下一个节点"同时"收到两个力的时候才不会倒下，否则会直接倒下
                        force_dir[next_i].append(force_dir[i][0])
        print(ans)
        return ''.join(ans)


test = Solution()
test.pushDominoes("RR.L")
