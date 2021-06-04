class Solution:
    def decodeString(self, s: str) -> str:
        """
        思路：
        1. 题目中提到括号，那么明显可以使用堆栈方式处理
        2. []之间为一个栈的元素
        3. 注意multiplier是两位数的情况
        """
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':    
                #当左括号的时候push，其实这里貌似只push了multiplier
                #在最后做乘法的时候直接乘以后面整个括号
                #再入栈之后要清空buffer
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                #当有括号时候pop
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                #当数字为23的时候先扫描到2然后再扫描到3，因此要把2和3组合起来
                multi = multi * 10 + int(c) 
            else:
                res += c    #其他情况下延长res
        return res

class Solution:
    def decodeString(self, s: str) -> str:
        """
        思路：（递归解法）
        1. 使用[作为开始标志，]作为结束标志
        2. 当 s[i] == '[' 时，开启新一层递归，记录此 [...] 内字符串 tmp 和递归后的最新索引 i，并执行 res + multi * tmp 拼接字符串。
        """
        def dfs(s, i):
            res, multiplier = "", 0
            while i < len(s):
                if s[i] == "]": #如果遇到递归结束标志
                    return i, res #返回当前已经处理完的子串的坐标，不用重复遍历
                elif s[i] == "[":   #如果遇到递归开始标志
                    i, tmp = dfs(s, i + 1)   #从下一位开始递归
                    res = res + multiplier * tmp    #子串*multiplier
                    multiplier = 0 #在完成一个子串吼multiplier要置0，不然会重复
                elif "0" <= s[i] <= "9":
                    multiplier = 10 * multiplier + int(s[i]) #考虑两位数
                else:
                    res += s[i] #正常字符串这相加就好
                i += 1  #loop内index自增
            return res  #返回最后拼接完成的字符串
        return dfs(s, 0)    #程序的入口