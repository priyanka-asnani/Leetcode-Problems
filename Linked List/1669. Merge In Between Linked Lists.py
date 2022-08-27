# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = list1, list1
        dummy = ListNode(next=list1)
        
        # get the pointers to sublist that needs to be removed
        for i in range(a-1):
            start = start.next
        for i in range(b):
            end = end.next
            
        # iterate over the list2 
        curr = list2
        while curr and curr.next:
            curr = curr.next
        
        # do the merge
        start.next = list2
        curr.next = end.next
        
        return dummy.next
    
## Time Complexity: O(M+N)
## Space Complexity: O(1)