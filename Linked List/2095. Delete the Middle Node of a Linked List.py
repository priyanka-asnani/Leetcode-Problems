# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        if head.next is None:
            return None
        
        slow, fast = head, head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next = slow.next
        return head


## Time Complexity: O(N)
## Space Complexity: O(1)