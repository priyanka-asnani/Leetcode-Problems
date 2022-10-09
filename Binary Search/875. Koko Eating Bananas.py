class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.validSpeed(mid, piles, h):
                right = mid
            else:
                left = mid + 1
        return right

    def validSpeed(self, n_bananas, piles, h):
        hours_taken = 0
        for i in range(len(piles)):
            quotient = piles[i] // n_bananas
            if piles[i] % n_bananas == 0:
                hours_taken += quotient
            else:
                hours_taken += quotient + 1
        return hours_taken <= h

## Time Complexity: O(N log N)
## Space Complexity: O(1)