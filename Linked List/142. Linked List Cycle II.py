# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = self.intersection(head)
        if not slow:
            return None
        # find the starting point of the intersection 
        pointer1 = head
        pointer2 = slow
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
    
    # detect cycle  
    def intersection(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return slow
        return None
    

## Time Complexity: O(N)
## Space Complexity: O(1)
            
        