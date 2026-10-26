# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        cnt = 0

        while cnt < k:
            if temp == None:
                return head

            temp = temp.next
            cnt += 1

        newNode = self.reverseKGroup(temp, k)

        temp = head
        cnt = 0

        while cnt < k:
            next = temp.next
            temp.next = newNode
            newNode = temp
            temp = next

            cnt += 1

        
        return newNode


