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
        if not root:
            return 0
        
        level = 0
        
        q = deque([root])
        while q:
            num_nodes = len(q)
            level += 1
            for i in range(num_nodes):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
        return level
        
## Time Complexity: O(N)
## Time Complexity: O(M)