# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        max_total = float(-inf)
        level = 0
        
        q = deque([root])
        while q:
            num_nodes = len(q)
            total = 0
            level += 1
            for i in range(num_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                total += node.val
            if total > max_total:
                max_total = total
                max_level = level
        return max_level
    
## Time Complexity: O(N)
## Space Complexity: O(M)