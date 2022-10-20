class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        result.append(nums[0])
        for i in range(1, len(nums)):
            prefix_sum = nums[i] + result[i-1]
            result.append(prefix_sum)
        return result

## Time Complexity: O(N)
## Space Complexity: O(N)
