class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            target = 2 * arr[i]
            left, right = i+1, len(arr) - 1
            if target < 0:
                left, right = 0, i-1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    return True
                elif target > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

## Time Complexity: O(N log N)
## Space Complexity: O(1)
        