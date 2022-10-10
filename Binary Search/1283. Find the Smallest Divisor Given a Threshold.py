class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        min_index = float(inf)
        while left <= right:
            mid = left + (right - left) // 2
            if self.validSum(mid, nums, threshold):
                min_index = min(min_index, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_index

    def validSum(self, divisor, nums, threshold):
        current_total = 0
        for number in nums:
            quotient = number // divisor
            if number % divisor == 0:
                current_total += quotient
            else:
                current_total += quotient + 1
        return current_total <= threshold

## Time Complexity: O(N log M)
## Space Complexity: O(1)