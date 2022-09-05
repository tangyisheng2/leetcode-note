# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.max_capacity = capacity
#         self.cache = {}
#         self.usage_log = collections.deque()
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.usage_log.remove(key)
#             self.usage_log.append(key)
#             return self.cache[key]
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         if len(self.cache) >= self.max_capacity and key not in self.cache:  # 这里需要判断如果对cache内已有数据进行更新的时候数组长度不变
#             self.cache.pop(self.usage_log.popleft())
#         if key in self.usage_log:
#             self.usage_log.remove(key)
#         self.cache.update({key: value})
#         self.usage_log.append(key)


class D_LinkedList:
    """
    D_LinkedList只存储key的先后顺序，具体访问需要回到hashmap
    """

    def __init__(self):
        self.prev = None
        self.key = None
        self.val = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.hashmap = {}  # 创建哈希表用于查找

        self.head = D_LinkedList()  # 创建头尾节点
        self.tail = D_LinkedList()

        self.head.next = self.tail  # 头节点是最新访问的
        self.tail.prev = self.head

    def move_node_to_head(self, key):
        if key not in self.hashmap:
            return
        node = self.hashmap[key]
        node.prev.next = node.next  # 链接node前后的节点
        node.next.prev = node.prev  # ！！！这里prev不要打成prew了！！！

        # 将node插入到节点头
        node.prev = self.head  # node连接到链表头
        node.next = self.head.next
        self.head.next.prev = node  # 链表头连接到node
        self.head.next = node  # 原来链表的第一个节点连接到head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_head(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.val
        #     return self.node_mapping[key].val
        # else:
        #     return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_node_to_head(key)
            self.hashmap[key].val = value  # 更新哈希表中的值
        else:
            if len(self.hashmap) >= self.max_capacity:  # 如果cache的容量大于等于最大容量还需要插入时
                self.hashmap.pop(self.tail.prev.key)  # 哈希表去掉最尾的节点
                last_node = self.tail.prev
                last_node.prev.next = self.tail
                self.tail.prev = last_node.prev


            node = D_LinkedList()  # 新建节点并插入到链表头

            self.hashmap.update({key: node})

            node.key = key
            node.val = value
            node.prev = self.head
            node.next = self.head.next

            self.head.next.prev = node  # 链接前后节点
            self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.max_capacity = capacity
#         self.cache = {}  # 存储节点信息
#         self.head = Node()  # 链表头部
#         self.tail = Node()  # 链表尾部
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             node = self.cache[key]  # 取得节点
#
#             pre_node, next_node = node.prev, node.next  # 删除节点
#             pre_node.next = next_node
#             next_node.prev = pre_node
#
#             node.next = self.head.next  # 重新链接链表
#             node.next.prew = node
#             self.head.next = node
#
#             return node.val
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         if len(self.cache) >= self.max_capacity and key not in self.cache:  # 超出了最大长度且需要新增数据
#             last_node = self.cache[self.tail.prev.key]  # 获取最后的节点
#             self.cache.pop(last_node.key)  # 从cache中删除最后节点
#             last_node.prev.next = self.tail  # 倒数第二个节点链接队列尾
#             self.tail.prev = last_node.prev  # 队列尾链接倒是第二个节点
#
#         node = Node()  # 构建节点
#         node.key = key
#         node.val = value
#
#         node.prev = self.head  # prev链接链表头
#         node.next = self.head.next  # next链接原链表头（插入后的第二个节点）
#
#         node.next.prev = node  # 插入后的第二个节点链接node
#         self.head.next = node  # 链表头指向第一个节点node
#
#         self.cache.update({key, node})


class D_Linklist:
    def __init__(self):
        self.prev = None
        self.key = None
        self.val = None
        self.next = None


class LRUCache2:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.capacity = 0
        # For get in O(1), use hashmap
        self.map = {}
        # For modify order in O(1), use doubly linked list
        self.head = D_Linklist()
        self.tail = D_Linklist()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def insert_node_top(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            self.insert_node_top(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            # Note that when we update a record, the current capacity does not change
            self.capacity -= 1
        new_node = D_Linklist()
        new_node.key = key
        new_node.val = value
        self.insert_node_top(new_node)
        self.map[key] = new_node
        self.capacity += 1
        if self.capacity > self.max_capacity:
            node_to_remove = self.tail.prev
            self.remove_node(node_to_remove)
            del self.map[node_to_remove.key]
            self.capacity -= 1


def printLinkedlist(head):
    node = head.next
    res = f"Head"
    while node.next:
        res = f"{res}->{node.key}"
        node = node.next
    print(res)
    return res


op = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
val = [[2], [1, 1], [2, 2], [2], [3, 3], [2], [4, 4], [1], [3], [4]]
test = LRUCache(0)
for operator, value in zip(op, val):
    pass
    if operator == "LRUCache":
        test = LRUCache(value[0])
        print(None)
    elif operator == "put":
        test.put(key=value[0], value=value[1])
        print(None)
    elif operator == "get":
        ret = test.get(key=value[0])
        print(ret)
    # print(printLinkedlist(test.head))
