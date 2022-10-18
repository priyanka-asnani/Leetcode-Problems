class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        array_sum = 0
        for i in range(n+1):
            total_sum += i

        for j in range(len(nums)):
            array_sum += nums[j]
        
        # return difference of two arrays
        return total_sum - array_sum

## Time Complexity: O(N)
## Space Complexity: O(1)