# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        result = []
        
        # initialize queue
        q = deque([root])
        while q:
            num_nodes = len(q)
            largest = float(-inf)
            for i in range(num_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                largest = max(largest, node.val)
            result.append(largest)
    
        return result
    
## Time Complexity: O(N)
## Space Complexity: O(M)