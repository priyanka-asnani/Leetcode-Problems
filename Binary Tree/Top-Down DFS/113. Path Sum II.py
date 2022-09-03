# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return None
        
        result = []
        
        def dfs(node, target, slate):
            target = target - node.val
            slate.append(node.val)
            
             # leaf node
            if not node.left and not node.right:
                if target == 0:
                    result.append(slate[:])
                    
            # recursive case
            if node.left:
                dfs(node.left, target, slate)
            if node.right:
                dfs(node.right, target, slate)
            slate.pop()   
            return
        
        dfs(root, targetSum, [])
        
        return result
    
## Time Complexity: O(N)
## Space Complexity: O(N)