class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def insert(self, node):
        self.cache[node.key] = node

    def removeLRU(self):
        self.cache.pop(next(iter(self.cache)))

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache.pop(key)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.removeLRU()
        self.insert(Node(key, value))