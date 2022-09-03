# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def dfs(node):
            
            # base case
            if not node.left and not node.right:
                return 0
            
            # recursive case
            max_height, longest_path = 0, 0
            if node.left:
                left_height = dfs(node.left)
                longest_path += 1 + left_height
                max_height = max(max_height, 1 + left_height)
                
            if node.right:
                right_height = dfs(node.right)
                longest_path += 1 + right_height
                max_height = max(max_height, 1 + right_height)
            
            # update the longest path
            diameter[0] = max(diameter[0], longest_path)
            return max_height
        
        dfs(root)
        return diameter[0]
    
## Time Complexity: O(N)
## Space Complexity: O(N)
                
        