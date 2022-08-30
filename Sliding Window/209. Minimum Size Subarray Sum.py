class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ## Sliding Window Approach
        left, total = 0, 0
        min_length = float(inf)
        # iterate over the list
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                # length of the window
                length = right - left + 1
                min_length = min(min_length, length)
                total -= nums[left]
                left += 1
        return 0 if min_length == float(inf) else min_length
    
## Time Complexity: O(N)
## Space Complexity: O(1)