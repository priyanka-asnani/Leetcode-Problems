class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ## using recursion
        result = []
        def helper(nums, i, slate):
            # base case
            if i == len(nums):
                result.append(slate[:])
                return
            
            # recursive case
            hashset = set()
            for pick in range(i, len(nums)):
                nums[pick], nums[i] = nums[i], nums[pick]
                if nums[i] not in hashset:
                    slate.append(nums[i])
                    helper(nums, i+1, slate)
                    slate.pop()
                    hashset.add(nums[i])
                nums[pick], nums[i] = nums[i], nums[pick]               
        helper(nums, 0, [])
        return result
    
## Time Complexity: O(N! * N)
## Space Complexity: O(N! * N)