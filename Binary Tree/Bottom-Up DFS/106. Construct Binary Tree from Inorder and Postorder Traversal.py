# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
            
        def helper(postorder, pstart, pend, inorder, istart, iend):
            # base case
            if pstart > pend:
                return None
            if pstart == pend:
                return TreeNode(postorder[pstart])
            
            # recursive case
            root = TreeNode(postorder[pend])
            # find the index of root from the hashmap
            rootindex = hashmap[postorder[pend]]
            numleft = rootindex - istart
            numright = iend - rootindex
            # recursively call helper function to construct left and right subtrees
            root.left = helper(postorder, pstart, pstart + numleft - 1, inorder, istart, rootindex - 1)
            root.right = helper(postorder, pstart + numleft, pend - 1, inorder, rootindex+1, iend)
            return root
        
        return helper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)
    
## Time complexity: O(N)
## Space complexity: O(N)