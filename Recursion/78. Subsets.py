class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # using rescursion
        result = []
        def helper(nums, i, slate):
            # base case
            if i == len(nums):
                result.append(slate[:])
                return
            
            # recursive case
            slate.append(nums[i])
            helper(nums, i+1, slate)
            slate.pop()
            helper(nums, i+1, slate)
            return
        helper(nums, 0, [])
        return result
    
## Time Complexity: O(2^N * N)
## Space Complexity: O(2^N * N)