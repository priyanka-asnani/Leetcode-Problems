class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using cycle sort
        for i in range(len(nums)):
            while nums[i] != i:
                dest = nums[i]
                if nums[i] != nums[dest]:
                    nums[i], nums[dest] = nums[dest], nums[i]
                else: break

        for i in range(len(nums)):
            if nums[i] != i:
                return nums[i] 

## Time Complexity: O(N)
## Space Complexity: O(1)