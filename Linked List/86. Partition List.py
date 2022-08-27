# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # create sublist nodes
        right = ListNode()
        left = ListNode()
        curr_right, curr_left = right, left
        
        # iterate over the list
        curr = head
        while curr:
            if curr.val >= x:
                curr_right.next = curr
                curr_right = curr_right.next
            else:
                curr_left.next = curr
                curr_left = curr_left.next
            curr = curr.next
                
        # combine two sublist to form new list
        curr_left.next = right.next
        curr_right.next = None
        return left.next
    
## Time Complexity: O(N)
## Space Complexity: O(1)