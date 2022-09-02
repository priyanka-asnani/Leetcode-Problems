# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        result = []
        
        # initialize queue
        q = deque([root])
        while q:
            num_nodes = len(q)
            right_node = None
            for i in range(num_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                right_node = node.val
            # append the last element at each level
            result.append(right_node)
        
        return result
    
## Time Complexity: O(N)
## Space Complexity: O(M)