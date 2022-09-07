# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        result = []
        # serializing using pre-order traversal
        def dfs(node):
            result.append(str(node.val))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            return
        dfs(root)
        return ','.join(result)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None
        
        splitdata = data.split(',')
        nums = [int(string) for string in splitdata]
        preorder = nums
        inorder = sorted(preorder)
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
            root = TreeNode(preorder[pstart])
            rootindex = hashmap[preorder[pstart]]
            numsleft = rootindex - istart
            numsright = iend - rootindex
            
            # recursively call helper functions to construct left and right subtrees
            root.left = helper(preorder, pstart + 1, pstart + numsleft, inorder, istart, rootindex - 1)
            root.right = helper(preorder, pstart + numsleft + 1, pend, inorder, rootindex + 1, iend)
            return root
            
        return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
    
## Time Complexity: O(N)
## Space Complexity: O(N)