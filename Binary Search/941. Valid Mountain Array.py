class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        n = len(arr)
        i = 0
        # walk up
        while i+1 < n and arr[i+1] > arr[i]:
            i += 1 

        # either there was never an increasing sequence
        # or there was only the increasing sequence and we reached the end of array
        if i == 0 or i == n-1:
            return False

        # walk down
        while i+1 < n and arr[i] > arr[i+1]:
            i += 1

        return i == n-1

## Time Complexity: O(N)
## Space Complexity: O(1)
    