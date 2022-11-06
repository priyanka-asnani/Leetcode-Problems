class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        index = right
        while left <= right:
            mid = left + (right - left) // 2
            if mid+1 < len(nums) and nums[mid+1] < nums[mid]:
                # record the peak index
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        return index


## Time Complexity: O(log N)
## Space Complexity: O(1)
