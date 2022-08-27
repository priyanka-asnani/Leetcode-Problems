# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Two-Pointer Approach
        if not head:
            return None
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # move pointer till end of duplicates sublist
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # skip all duplicates
                prev.next = curr.next 
            else:
                prev = curr
            curr = curr.next
        return dummy.next
    
## Time Complexity: O(N)
## Space Complexity: O(1)