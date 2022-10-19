class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.startIndex(nums, target)
        end = self.endIndex(nums, target)
        if start == -1 and end == -1:
            return [-1, -1]
        else:
            return [start, end]

    def startIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        startindex = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                startindex = mid
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return startindex

    def endIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        endindex = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                endindex = mid
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return endindex

## Time Complexity: O(log N)
## Space Complexity: O(1)