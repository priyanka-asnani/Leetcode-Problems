# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        global_balanced = [True]
        
        if not root:
            return global_balanced[0]
        
        def dfs(node):
            # base case
            if not node.left and not node.right:
                return 0
            
            # recursive case
            max_height, left_height, right_height = 0, 0, 0
            if node.left:
                left_height = 1 + dfs(node.left)
                max_height = max(max_height, left_height)
            if node.right:
                right_height = 1 + dfs(node.right)
                max_height = max(max_height, right_height)
                
            # update the global_balanced variable if the subtree is not balanced
            if abs(left_height - right_height) > 1:
                global_balanced[0] = False
       
            return max_height
        
        dfs(root)
        return global_balanced[0]
    
## Time Complexity: O(N)
## Space Complexity: O(N)