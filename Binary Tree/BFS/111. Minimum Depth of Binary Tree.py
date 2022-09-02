# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        
        # initialize a queue
        q = deque([root])
        while q:
            num_nodes = len(q)
            level += 1
            for i in range(num_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if not node.left and not node.right:
                    return level
        return None
    
## Time Complexity: O(N)
## Space Complexity: O(M)