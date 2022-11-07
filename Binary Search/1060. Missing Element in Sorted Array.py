class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        start = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            num_missing = nums[mid] - mid - start
            if num_missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return (nums[right - 1] + k) - (nums[right - 1] - right - start)

## Time Complexity: O(log N)
## Time Complexity: O(1)