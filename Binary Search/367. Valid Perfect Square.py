class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        left = 2
        right = num // 2 
        while left <= right:
            mid = left + (right - left) // 2
            guess_square = mid * mid
            if guess_square == num:
                return True
            elif num < guess_square :
                right = mid - 1
            else:
                left = mid + 1
        return False

## Time Complexity: O(log N)
## Space Complexity: O(1)