# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2lists(self , l1 , l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.merge2lists(l1.next , l2)
            return l1
        else:
            l2.next = self.merge2lists(l1 , l2.next)
            return l2

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)
        if k <= 1:
            return None
        ans = lists[0]


        for i in range(1, k ):
            ans = self.merge2lists(ans , lists[i])
        
        return ans












        # s = 0 
        # e = len(lists) - 1

        # if s == e:
        #     return lists[s]

        # m = (s + (e - s) )// 2

        # part1 = self.mergeKLists([lists[s] , lists[m]])
        # part2 = self.mergeKlists([lists[m+1] , lists[e]])

        # return merge2lists(part1,part2)








