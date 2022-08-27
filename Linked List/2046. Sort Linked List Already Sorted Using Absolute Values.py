# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right = ListNode()
        left = ListNode()
        rtail, ltail = right, left
        curr = head
        # create two sublists
        while curr:
            if curr.val > 0:
                rtail.next = curr
                rtail = rtail.next
            else:
                ltail.next = curr
                ltail = ltail.next
            curr = curr.next
        rtail.next = None;
        ltail.next = None;
            
        # reverse left sublist
        lhead = left.next
        prev = None
        while lhead:
            temp = lhead.next
            lhead.next = prev
            prev = lhead
            lhead = temp
            
        if left.next is None:
            return right.next;
        
        # update the pointers
        left.next.next = right.next
        return prev
    
        
                 
        
## Time Complexity: O(N)
## Time Complexity: O(1)