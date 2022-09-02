# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        
        result = []
        
        # initialize queue
        q = deque([root])
        while q:
            num_nodes = len(q)
            total = 0
            for i in range(num_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                total += node.val
            # comute average of nodes at each level and append it to result list
            result.append(total/num_nodes)
            
        return result
    
## Time Complexity: O(N)
## Time Complexity: O(N)