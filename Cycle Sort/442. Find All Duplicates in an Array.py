class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # using cycle sort
        result = []
        for i in range(len(nums)):
            while nums[i] != i+1:
                dist = nums[i] - 1
                if nums[i] != nums[dist]:
                    nums[i], nums[dist] = nums[dist], nums[i]
                else: break

        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(nums[i])
        return result

## Time Complexity: O(N)
## Time Complexity: O(1)