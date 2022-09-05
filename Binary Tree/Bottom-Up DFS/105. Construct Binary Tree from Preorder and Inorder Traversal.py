# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
            
        def helper(preorder, pstart, pend, inorder, istart, iend):
            # base case
            if pstart > pend:
                return None
            if pstart == pend:
                return TreeNode(preorder[pstart])
            
            # recursive case
            # find the index of root in the hashmap
            root = TreeNode(preorder[pstart])
            rootindex = hashmap[preorder[pstart]]
            numleft = rootindex - istart
            numright = iend - rootindex
            root.left = helper(preorder, pstart + 1, pstart + numleft, inorder, istart, rootindex - 1)
            root.right = helper(preorder, pstart + numleft + 1, pend, inorder, rootindex + 1, iend)
            return root
        
        return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
    
## Time Complexity: O(N)
## Space Complexity: O(N)
        