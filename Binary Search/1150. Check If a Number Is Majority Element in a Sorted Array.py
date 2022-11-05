class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        start = self.startIndex(nums, target)
        end = self.endIndex(nums, target)
        count = (end - start) + 1
        if start == -1 and end == -1: return False
        if count > len(nums) // 2 : return True

    def startIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        start_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start_index = mid
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else: right = mid - 1
        return start_index

    def endIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        end_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                end_index = mid
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else: right = mid - 1
        return end_index

## Time Complexity: O(log N)
## Space Complexity: O(1)