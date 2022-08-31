  ## Sliding Window Approach
        max_sum = float(-inf)
        left, window_sum = 0, 0
        for i in range(len(nums)):
            window_sum += nums[i]
            # length of window exceeded k
            if i >= k-1:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[left]
                left += 1
        return max_sum/k
    
## Time Complexity: O(N)
## Space Complexity: O(1)
                