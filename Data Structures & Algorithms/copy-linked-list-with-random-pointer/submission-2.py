"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        cur = head

        while cur:
            clone = Node(cur.val, cur.next)
            cur.next = clone

            # cur = cur.next.next
            cur = clone.next

        cur = head
        while cur:
            clone = cur.next
            # important point to be checked here
            # here we need to check if the random even exists or not
            # because if the random pointer of the cur in NONE
            # when we access None.next it is going to throw an error
            if cur.random:
                clone.random = cur.random.next
            cur = clone.next

        cur = head
        # because we inserted the cloned head at the cur.next thats why we store  
        # header as cur .next
        clone_header = cur.next

        while cur:
            clone = cur.next
            cur.next = cur.next.next
            clone.next = clone.next.next if clone.next else None         

            cur = cur.next

        return clone_header
