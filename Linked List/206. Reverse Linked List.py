# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Two-pointer Approach
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        return prev

## Time Complexity: O(N)
## Space Complexity: O(1)