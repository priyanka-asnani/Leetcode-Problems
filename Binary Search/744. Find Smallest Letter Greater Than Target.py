class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        result = letters[0]
        while left <= right:
            mid = left + (right - left) // 2
            if target < letters[mid]:
                result = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        return result

## Time Complexity: O(log N)
## Space Complexity: O(1)