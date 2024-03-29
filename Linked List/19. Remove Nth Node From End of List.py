# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of linked list
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        # Remove the nth node feom list
        dummy = ListNode(next=head)
        prev, cur = dummy, head
        index = count - n + 1
        for i in range(index - 1):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return dummy.next
            
## Time Complexity: O(N)
## Space Complexity: O(1)