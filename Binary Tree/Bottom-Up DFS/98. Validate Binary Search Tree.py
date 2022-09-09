# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        
        is_bst = [True]
        
        def dfs(node):
            amibst = True
            smallest, largest = node.val, node.val
            
            # base case
            if not node.left and not node.right:
                return (smallest, largest, amibst)
            
            # recursive case
            if node.left:
                (s, l, b) = dfs(node.left)
                # update the smallest value
                smallest = min(smallest, s)
                # update the largest value
                largest = max(largest, l)
                if not b or node.val <= l:
                    amibst = False
                    
            if node.right:
                (s, l, b) = dfs(node.right)
                # update the smallest value
                smallest = min(smallest, s)
                # update the largest value
                largest = max(largest, l)
                if not b or node.val >= s:
                    amibst = False
                    
            if not amibst:
                is_bst[0] = False
                
            return (smallest, largest, amibst)
        
        dfs(root)
        return is_bst[0]

## Time Complexity: O(N)
## Space Complexity: O(N)