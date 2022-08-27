# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        curr = head
        while curr:
            result = result * 2
            result = result + curr.val
            curr = curr.next
        return result
    
## Time Complexity: O(N)
## Space Complexity: O(1)