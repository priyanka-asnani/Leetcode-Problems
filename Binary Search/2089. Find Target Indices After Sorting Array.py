class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start = self.findStartIndex(nums, target)
        end = self.findEndIndex(nums, target)
        if start == -1 and end == -1:
            return []
        result = []
        for i in range(start, end+1):
            result.append(i)
        return result

    def findStartIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        start_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start_index = mid
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return start_index

    def findEndIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        end_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                end_index = mid
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return end_index

## Time Complexity: O(log N)
## Space Complexity: O(1)