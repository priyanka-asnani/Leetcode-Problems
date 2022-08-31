class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Sliding Window Approach
        max_len, left = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                # move left pointer
                left = right + 1
            else:
                max_len = max(max_len, right - left + 1)
        return max_len
    
## Time Complexity: O(N)
## Space Complexity: O(1)
                