# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right
        curr = head
        odd = True
        
        # iterate over the list
        while curr:
            if odd == True:
                ltail.next = curr
                ltail = ltail.next
                odd = False
            else:
                rtail.next = curr
                rtail = rtail.next
                odd = True
            curr = curr.next
            
        # Connect the two sublist
        ltail.next = right.next
        rtail.next = None
        return left.next
    
## Time Complexity: O(N)
## Time Complexity: O(1)