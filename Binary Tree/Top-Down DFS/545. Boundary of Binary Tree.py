# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        elif not root.left and not root.right:
            return [root.val]
        
        # collect nodes in the left boundary
        left_boundary = [root.val]
        if root.left:
            curr = root.left
            while curr:
                left_boundary.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        if len(left_boundary) > 1:
            left_boundary.pop()
        
         # collect nodes in the right boundary
        right_boundary = []
        if root.right:
            curr = root.right
            while curr:
                right_boundary.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
                    
        if right_boundary:
            right_boundary.pop()
        right_boundary.reverse()
        
          
        # collect leaves from left to right
        leaves = []
        def dfs(node):
            # base case
            if not node.right and not node.left:
                leaves.append(node.val)
                
            # recursive case
            if node.left:
                dfs(node.left) 
            if node.right:
                dfs(node.right) 
        
        dfs(root)
        
        return left_boundary + leaves + right_boundary
    
## Time Complexity: O(N)
## Space Complexity: O(N)
        