import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cache = {}
        self.usage_log = collections.deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usage_log.remove(key)
            self.usage_log.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.max_capacity and key not in self.cache:  # 这里需要判断如果对cache内已有数据进行更新的时候数组长度不变
            self.cache.pop(self.usage_log.popleft())
        if key in self.usage_log:
            self.usage_log.remove(key)
        self.cache.update({key: value})
        self.usage_log.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
op = ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
val = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
test = LRUCache(0)
for operator, value in zip(op, val):
    if operator == "LRUCache":
        test = LRUCache(value[0])
        print(None)
    elif operator == "put":
        test.put(key=value[0], value=value[1])
        print(None)
    elif operator == "get":
        ret = test.get(key=value[0])
        print(ret)
