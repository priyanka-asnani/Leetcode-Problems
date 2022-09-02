# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        result = []
        ltor = True
        
        # initalize queue
        q = deque([root])
        while q:
            num_nodes = len(q)
            temp = []
            for i in range(num_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            if ltor == False:
                result.append(temp[::-1])
                ltor = True
            else:
                result.append(temp)
                ltor = False
        return result

## Time Complexity: O(N)
## Space Complexity: O(N)