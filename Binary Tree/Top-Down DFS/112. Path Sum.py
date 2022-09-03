# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:  
        if not root:
            return False
        
        result = [False]
        
        def dfs(node, target):
            target = target - node.val
            # base case
            if not node.left and not node.right:
                if target == 0:
                    result[0] = True 
            
            # recursive case
            if node.left:
                dfs(node.left, target)
            if node.right:
                dfs(node.right, target)
            return
                
        dfs(root, targetSum)
        return result[0]
    
## Time Complexity: O(N)
## Time Complexity: O(N)