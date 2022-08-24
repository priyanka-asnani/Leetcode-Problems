# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ## Two-Pointer Approach
        # create a new dummy node
        dummy = ListNode(next = head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                # update the prev pointer
                prev.next = curr.next
            else:
                prev = curr
            # move the curr pointer
            curr = curr.next
        return dummy.next
    
## Time Complexity: O(N)
## Space Complexity: O(1)