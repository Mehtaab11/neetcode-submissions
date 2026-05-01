# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-1)
        dummy = prev

        carry = 0 
        while l1 or l2:
            if l1:
                carry += l1.val
            if l2:
                carry += l2.val

            newNode = ListNode(carry%10)

            carry = carry // 10

            prev.next = newNode
            prev= prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            newNode = ListNode(carry%10)
            prev.next = newNode

        return dummy.next

