class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == mid:
                index = mid
                right = mid - 1
            elif mid > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1 
        return index

## Time Complexity: O(log N)
## Space Complexity: O(1)