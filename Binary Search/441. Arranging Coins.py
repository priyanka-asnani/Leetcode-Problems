class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = left + (right - left) // 2
            coins = (k * (k+1)) // 2
            if coins == n:
                return k
            elif n > coins:
                left = k + 1
            else:
                right = k - 1
        return right

## Time Complexity: O(log N)
## Space Complexity: O(1)