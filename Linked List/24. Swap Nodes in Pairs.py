# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr, prev = head, dummy
        while curr and curr.next:
            # initialize pointers
            first_node = curr
            second_node = curr.next
            # swap nodes
            first_node.next = second_node.next
            second_node.next = first_node
            prev.next = second_node
            # update pointers
            prev = first_node
            curr = first_node.next
        return dummy.next

## Time Complexity: O(N)
## Space Complexity: O(1)