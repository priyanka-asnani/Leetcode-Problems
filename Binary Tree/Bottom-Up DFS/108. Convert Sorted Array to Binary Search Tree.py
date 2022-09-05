# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Bottom-Up approach
        def helper(arr, start, end):
            # base case
            if start > end:
                return None
            
            if start == end:
                return TreeNode(arr[start])
            
            # recursive case
            mid = start + (end - start) // 2
            root = TreeNode(arr[mid])
            root.left = helper(arr, start, mid-1)
            root.right = helper(arr, mid+1, end)
            return root
        
        return helper(nums, 0, len(nums) - 1)
        
## Time Complexity: O(N)
## Space Complexity: O(log N)