class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float(inf)
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break
            mid = left + (right - left) // 2
            minimum = min(minimum, nums[mid])
            # mid in first half
            if nums[mid] >= nums[left]:
                left = mid + 1
            # mid in second half
            else:
                right = mid - 1
        return minimum

## Time Complexity: O(log N)
## Space Complexity: O(1)