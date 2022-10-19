class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using cycle sort
        for i in range(len(nums)):
            while nums[i] != i:
                dist = nums[i]
                if dist < len(nums):
                    nums[i], nums[dist] = nums[dist], nums[i]
                else: break

        for i in range(len(nums)):
            if nums[i] == len(nums):
                return i
        return len(nums)

## Time Complexity: O(N)
## Time Complexity: O(1)