# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base cases
        if not head: return None
        if not head.next: return head
        
        # get the length of linked list
        tail = head
        before_tail = None
        length = 0
        while tail:
            length += 1
            before_tail = tail
            tail = tail.next
        k = k % length
        if k == 0:
            return head
        
        # move to the pivot and rotate
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        # update the pointers
        new_head = curr.next
        curr.next = None
        before_tail.next = head
        return new_head
        
    
## Time Complexity: O(N)
## Space Complexity: O(1)