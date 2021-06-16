# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        从题目中的ListNode与实际运算的数字反向
        我们可以使用堆栈数据结构的先入先出特性来将数字反序并进行相加
        """
        l1_stack, l2_stack = [], []  # 新建堆栈
        l1_res, l2_res = 0, 0  # 新建两个变量存储l1, l2用于计算的值
        while l1:
            l1_stack.append(l1.val)  # l1中元素逐个入栈
            l1 = l1.next  # l1指针后移
        while l1_stack:
            l1_res = l1_stack.pop() + l1_res * 10  # l1栈中元素逐个出栈，并且相加获得l1数字
        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next
        while l2_stack:
            l2_res = l2_stack.pop() + l2_res * 10

        res = l1_res + l2_res  # 进行运算

        res = list(str(res))  # 这里将运算完成的结果转为str方便拆分成list
        res_stack = []

        for i in range(len(res)):
            res_stack.append(int(res[i]))  # 转换结果入栈，准备倒序处理

        res_listnode = ListNode()
        res_listnode_ptr = res_listnode
        while res_stack:
            num = res_stack.pop()  # 数组出栈
            res_listnode_ptr.val = num  # 构造链表
            if res_stack:  # 检测插入完节点之后还有没有多余的元素，如果没有就不需要在新建next域了
                res_listnode_ptr.next = ListNode()  # 链接链表的下一个节点
                res_listnode_ptr = res_listnode_ptr.next

        return res_listnode


# L1
l1 = ListNode()
l1.val = 2
l1.next = ListNode()
l1_tmp = l1.next
l1_tmp.val = 4
l1_tmp.next = ListNode()
l1_tmp = l1_tmp.next
l1_tmp.val = 3
# L2
l2 = ListNode()
l2.val = 5
l2.next = ListNode()
l2_tmp = l2.next
l2_tmp.val = 6
l2_tmp.next = ListNode()
l2_tmp = l2_tmp.next
l2_tmp.val = 4
test = Solution()
test.addTwoNumbers(l1, l2)
