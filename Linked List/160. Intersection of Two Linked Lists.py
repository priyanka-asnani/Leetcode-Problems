# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        while currA != currB:
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next
        return currA
                

                
## Time Complexity: O(M+N)
## Space Complexity: O(1)