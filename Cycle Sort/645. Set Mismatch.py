class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # use cycle sort
        for i in range(len(nums)):
            while nums[i] != i+1:
                dist = nums[i] - 1
                if nums[i] != nums[dist]:
                    nums[i], nums[dist] = nums[dist], nums[i]
                else: break

        for i in range(len(nums)):
            if nums[i] != i+1:
                return [nums[i], i+1]

## Time Complexity: O(N)
## Space Complexity: O(1)