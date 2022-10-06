class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            negatives = self.binarySearch(grid[i])
            result += negatives
        return result
        
    def binarySearch(self, row):
        count = len(row)
        left, right = 0, len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] >= 0:
                left = mid + 1
            else:
                right = mid - 1
        return count - left

## Time Complexity: O(log N)
## Space Complexity: O(1)