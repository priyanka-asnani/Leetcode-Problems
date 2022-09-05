# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(head):
            # base case
            if not head:
                return None
            
            if not head.next:
                return TreeNode(head.val)
            
            # recursiive case
            # get middle of the list
            left, slow = getMiddle(head)
            left.next = None
            right = slow.next
            root = TreeNode(slow.val)
            root.left = helper(head)
            root.right = helper(right)
            return root
            
            
        def getMiddle(head):
            slow, fast = head, head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return (prev, slow)
        
        return helper(head)   
    
## Time Complexity: O(NlogN)
## Space Complexity: O(logN)