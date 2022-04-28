#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :232. Implement Queue using Stacks.py
# @Time      :4/27/22
# @Author    :Eason Tang
class MyQueue:

    def __init__(self):
        self.start_idx = 0
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        ans = self.q[self.start_idx]
        self.start_idx += 1
        return ans

    def peek(self) -> int:
        return self.q[self.start_idx]

    def empty(self) -> bool:
        return self.start_idx > len(self.q) - 1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
