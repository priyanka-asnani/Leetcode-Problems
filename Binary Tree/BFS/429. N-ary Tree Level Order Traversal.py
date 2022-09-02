"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        
        result = []
        
        # initialize queue
        q = deque([root])
        while q:
            num_nodes = len(q)
            temp =[]
            for i in range(num_nodes):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
                temp.append(node.val)
            result.append(temp)
            
        return result
    
## Time Complexity: O(N)
## Space Complexity: O(N)