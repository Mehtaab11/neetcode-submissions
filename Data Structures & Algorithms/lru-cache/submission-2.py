class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.next = self.left.next
        node.prev = self.left
        self.left.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
            self.insert(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.right.prev
            self.remove(lru_node)

            del self.cache[lru_node.key]
    