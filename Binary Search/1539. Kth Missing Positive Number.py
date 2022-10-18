class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # using Binary Search
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            num_missing = arr[mid] - mid - 1
            if num_missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return (arr[right] + k)  - (arr[right] - right - 1)

## Time Complexity: O(log N)
## Space Complexity: O(1)