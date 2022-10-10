class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 1
        count = 0
        while left < len(nums) and right < len(nums):
            diff = nums[left] - nums[right]
            if (left >= right) or abs(diff) < k:
                right += 1
            elif abs(diff) > k:
                left += 1
            else:
                count += 1
                left += 1
                while left < len(nums) and nums[left - 1] == nums[left]:
                    left += 1
        return count

## Time Complexity: O(N log N)
## Space Complexity: O(N)