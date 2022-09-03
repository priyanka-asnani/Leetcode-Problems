"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # top-down dfs approach
        if not root:
            return 0
        
        max_height = [0]
        
        def dfs(node, heightsofar):
            heightsofar += 1
            max_height[0] = max(max_height[0], heightsofar)
            
            # recursive case
            for child in node.children:
                dfs(child, heightsofar)
            return
        
        dfs(root, 0)
        return max_height[0]
    
## Time Complexity: O(N)
## Space Complexity: O(N)