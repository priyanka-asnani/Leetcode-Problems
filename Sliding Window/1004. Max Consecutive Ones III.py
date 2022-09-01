class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window Approach
        left, max_len = 0, 0
        zeroes_count = 0
        # iterate over the nums array
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes_count += 1
            window_len = right - left + 1
            # update max_len of the window
            if zeroes_count <= k:
                max_len = max(max_len, window_len)
            # if the window is invalid
            while zeroes_count > k:
                if nums[left] == 0:
                    zeroes_count -= 1
                left += 1      
        return max_len
    
## Time Complexity: O(N)
## Time Complexity: O(1)