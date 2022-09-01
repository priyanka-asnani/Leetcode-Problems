class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Sliding Window Approach
        left, zeroes_count = 0, 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes_count += 1
            window_length = right - left + 1
            # update the max length
            if zeroes_count <= 1:
                max_len = max(max_len, window_length)
                
            # if window is invalid
            while zeroes_count > 1:
                if nums[left] == 0:
                    zeroes_count -= 1
                left += 1
                
        return max_len
    
## Time Complexity: O(N)
## Time Complexity: O(1)