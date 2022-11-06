class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid-1]:
                # check if no of elements on the right side are even
                if (right - mid) % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1
            elif nums[mid] == nums[mid+1]:
                if (right - mid) % 2 == 0:
                    left = mid + 2
                else: 
                    right = mid - 1
            else:
                return nums[mid]
        return nums[left]

## Time Complexity: O(log N)
## Space Complexity: O(1)