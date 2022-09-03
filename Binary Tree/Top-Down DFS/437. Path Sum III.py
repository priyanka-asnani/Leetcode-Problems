# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        total = [0]
        
        def dfs(node, target, slate):
            # append the current node value to slate
            slate.append(node.val)
            
            # check every suffix sum to see if it's equal to target
            suffix_sum = 0
            for i in range(len(slate)-1, -1, -1):
                suffix_sum += slate[i]
                if suffix_sum == target:
                    total[0] += 1
                    
            # recursive case
            if node.left:
                dfs(node.left, target, slate)    
            if node.right:
                dfs(node.right, target, slate)
         
            slate.pop() 
            return
            
        dfs(root, targetSum, [])
        return total[0]
    
## Time Complexity: O(N)
## Space Complexity: O(N)