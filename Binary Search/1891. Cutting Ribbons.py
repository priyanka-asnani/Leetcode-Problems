class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left = 1
        right = max(ribbons)
        max_length = 0
        while left <= right:
            mid = left + (right - left) // 2
            n_ribbons = self.getTotalRibbons(mid, ribbons)
            if n_ribbons >= k:
                max_length = mid
                left = mid + 1
            else:
                right = mid - 1
        return max_length

    def getTotalRibbons(self, length, ribbons):
        total_ribbons = 0
        for i in range(len(ribbons)):
            quotient = ribbons[i] // length
            total_ribbons += quotient
        return total_ribbons

## Time Complexity: O(N log M)
## Time Complexity: O(1)