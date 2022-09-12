# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        largest_bst = [1]
        
        def dfs(node):
            amibst = True
            smallest, largest = node.val, node.val
            num_nodes = 1
            
            # base case
            if not node.left and not node.right:
                return (smallest, largest, amibst, num_nodes)
            
            # recursive case
            if node.left:
                (s, l, b, n) = dfs(node.left)
                num_nodes += n
                smallest = min(smallest, s)
                largest = max(largest, l)
                if not b or node.val <= l:
                    amibst = False
                    
            if node.right:
                (s, l, b , n) = dfs(node.right)
                num_nodes += n
                smallest = min(smallest, s)
                largest = max(largest, l)
                if not b or node.val >= s:
                    amibst = False
                    
            if amibst:
                largest_bst[0] = max(largest_bst[0], num_nodes)
                
            return (smallest, largest, amibst, num_nodes)
        
        dfs(root)
        return largest_bst[0]
        

## Time complexity: O(N)
## Space complexity: O(N)