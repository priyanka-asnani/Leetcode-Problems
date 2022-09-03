# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        global_max = [0]
        
        def dfs(node, pval, lengthsofar):
            if node.val == pval + 1:
                lengthsofar += 1
            else:
                lengthsofar = 1
                
            if lengthsofar > global_max[0]:
                global_max[0] = lengthsofar
            
            # recursive case
            if node.left:
                dfs(node.left, node.val, lengthsofar)
            if node.right:
                dfs(node.right, node.val, lengthsofar)
            return
        
        dfs(root, root.val, 0)
        return global_max[0]
    
## Time Complexity: O(N)
## Space Complexity: O(N)