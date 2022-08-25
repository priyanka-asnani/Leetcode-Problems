class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## using recursion
        result = []
        def helper(nums, i, slate):
            # base case
            if i == len(nums):
                result.append(slate[:])
                return
            
            # recursive case
            for pick in range(i, len(nums)):
                # swap the elements 
                nums[pick], nums[i] = nums[i], nums[pick]
                slate.append(nums[i])
                helper(nums, i+1, slate)
                slate.pop()
                nums[pick], nums[i] = nums[i], nums[pick]
            return
        
        helper(nums, 0, [])
        return result
    
## Time Complexity: O(N! * N)
## Space Complexity: O(N! * N)