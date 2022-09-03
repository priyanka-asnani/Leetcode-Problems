# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        
        def dfs(node):
            # swap its children
            old_left = node.left
            old_right = node.right
            node.left = old_right
            node.right = old_left
            
            # recursive case 
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            return
        
        dfs(root)
        return root
    
## Time Complexity: O(N)
## Space Complexity: O(N)