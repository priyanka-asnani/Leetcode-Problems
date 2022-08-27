# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        # base case for two elements
        if head.next.next is None:
            if head.val > head.next.val:
                head.val, head.next.val = head.next.val, head.val
            return head
        
        # split the list into two halves
        left = head
        right = self.findMiddle(head)
        temp = right.next
        right.next = None
        right = temp
        
        # sort the list recursively
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the two sorted halves
        return self.merge(left, right)
        
    def findMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def merge(self, left, right):
        curr = dummy = ListNode()
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next   
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return dummy.next
        
## Time Complexity: O(NlogN)
## Space Complexity: O(1)
        
                
        
            
        
        
        