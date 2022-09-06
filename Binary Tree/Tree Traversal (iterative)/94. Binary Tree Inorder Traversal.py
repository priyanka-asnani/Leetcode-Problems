# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative approach
        if not root:
            return None
        
        stack = []
        curr = root
        result = []
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            result.append(node.val)
            curr = node.right
        return result
    
## Time Complexity: O(N)
## Space Complexity: O(N)