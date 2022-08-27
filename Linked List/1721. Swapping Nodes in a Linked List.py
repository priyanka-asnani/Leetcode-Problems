# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the length of linked list
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next     
        # find index of the kth node from the end
        index = count - k + 1
        # swap values
        start, end = head, head
        for i in range(k-1):
            start = start.next
        for i in range(index-1):
            end = end.next
        start.val, end.val = end.val, start.val 
        return head
    
## Time Complexity: O(N)
## Space Complexity: O(1)