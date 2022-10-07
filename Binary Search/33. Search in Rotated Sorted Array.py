class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # mid in left sorted half
            if nums[mid] >= nums[left]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

            # mid in the right sorted half
            else:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1

## Time Complexity: O(log N)
## Space Complexity: O(1)
