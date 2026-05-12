class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.left = Node(0,0) 
        self.right= Node(0,0) 

        # Default pointers described in Node Class
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, Node):
        prv , nxt = Node.prev , Node.next

        prv.next = nxt
        nxt.prev = prv


    def insert(self, Node):
        prv = self.right.prev
        Node.next = self.right
        Node.prev = prv
        prv.next = self.right.prev = Node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            self.remove(node)
            self.insert(node)
            
            # beautiful But remember that before returning the value you should 
            # Make it the new Most Recently Used  
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

        newNode = Node(key,value)
        # Here u only did the insertion in the LL 
        # But u also need to map it to the key in hashmap
        self.cache[key] = newNode
        self.insert(newNode)
 
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]