class Node:
    def __init__(self, key, value):
        # Store key so we can delete it from hashmap during eviction
        self.key = key

        # Actual value of cache entry
        self.value = value

        # Doubly Linked List pointers
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        # Maximum size of cache
        self.cap = capacity

        # HashMap:
        # key -> node reference
        # Gives O(1) access
        self.cache = {}

        # Dummy left node  -> Least Recently Used side
        self.left = Node(0, 0)

        # Dummy right node -> Most Recently Used side
        self.right = Node(0, 0)

        # Initial connection:
        # left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):

        # Grab neighbors of current node
        prv, nxt = node.prev, node.next

        # Remove node from DLL
        # prv <-> node <-> nxt
        # becomes:
        # prv <-> nxt
        prv.next = nxt
        nxt.prev = prv

    def insert(self, node):

        # Insert node just before right
        # because right side represents MRU

        prv = self.right.prev

        # Form:
        # prv <-> node <-> right

        node.next = self.right
        node.prev = prv

        # Connect both sides
        prv.next = self.right.prev = node

    def get(self, key: int) -> int:

        # If key exists in cache
        if key in self.cache:

            node = self.cache[key]

            # Since key was accessed,
            # it becomes Most Recently Used

            self.remove(node)
            self.insert(node)

            return node.value

        # Key not found
        return -1

    def put(self, key: int, value: int) -> None:

        # If key already exists,
        # remove old node first
        if key in self.cache:

            node = self.cache[key]

            self.remove(node)

        # Create fresh node
        newNode = Node(key, value)

        # Store inside hashmap
        self.cache[key] = newNode

        # Insert at MRU position
        self.insert(newNode)

        # If cache exceeds capacity
        if len(self.cache) > self.cap:

            # Node next to left is LRU
            lru = self.left.next

            # Remove from DLL
            self.remove(lru)

            # Remove from hashmap
            del self.cache[lru.key]