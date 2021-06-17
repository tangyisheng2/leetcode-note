class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        符合要求的情况：
        1. 只有字符
        2. 若A和B是valid string，则AB也是valid string
        3. 可以在最外层包含括号
        思路：可以用栈来匹配内外的括号，如果出现孤立的右边括号则去除
        :param s: 修改前的pattern
        :return: 修改后的pattern
        """

        stack = []  # 创建用于匹配的堆栈
        s = list(s)  # 将str转换为数组方便我们遍历以及去除不匹配的括号

        for i in range(len(s)):
            if s[i] == "(":  # 左括号入栈
                stack.append(i)
            if s[i] == ")":  # 右括号时，栈内左括号出栈完成匹配
                if stack:  # 特殊情况：检测是不是空栈
                    stack.pop()
                else:  # 右括号没有匹配到的左括号，应该去除（左括号已经用完了）
                    s[i] = None  # 括号不匹配，先改成None
                    # 这里不直接pop的原因是pop会破坏原来的数组索引关系

        if stack:  # 特殊情况：检测完成之后还有左括号剩下，这些左括号也应该去除
            for i in stack:  # 如果stack内有没有匹配的左括号，那么这些括号也要去除
                s[i] = None

        return "".join(s[i] for i in range(len(s)) if s[i] is not None)  # 将剩下的字符拼接会字符串


test = Solution()
ret = test.minRemoveToMakeValid(s="lee(t(c)o)de)")
print(ret)
