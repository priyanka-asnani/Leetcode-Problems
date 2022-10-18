class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary Search Approach
        if x < 2:
            return x
        low = 0
        high = x // 2
        while low <= high:
            mid = low + (high - low) // 2
            nums = mid * mid
            if nums == x:
                return mid
            elif x > nums:
                low = mid + 1
            else:
                high = mid - 1
        return high

## Time Complexity: O(log N)
## Time Complexity: O(1)