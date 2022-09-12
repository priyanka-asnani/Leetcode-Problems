# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [None]
        
        def dfs(node, p, q):
            pfound, qfound = False, False
            if node is p:
                pfound = True
            if node is q:
                qfound = True
            # base case
            if not node.left and not node.right:
                return (pfound, qfound)
            
            # recursive case
            if node.left:
                is_pfound, is_qfound = dfs(node.left, p, q)
                pfound = pfound or is_pfound
                qfound = qfound or is_qfound
            if node.right:
                is_pfound, is_qfound = dfs(node.right, p, q)
                pfound = pfound or is_pfound
                qfound = qfound or is_qfound
            if pfound and qfound and not lca[0]:
                lca[0] = node
            return (pfound, qfound)
                
        dfs(root, p, q)
        return lca[0]
    
## Time Complexity: O(N)
## Space Complexity: O(N)