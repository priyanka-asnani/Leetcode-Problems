class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        i, j = 0, n-1
        total = 0
        while i < m and j >= 0:
            if grid[i][j] < 0:
                total += (m - i)
                # move the pointer to the left
                j -= 1
            # move to the next row
            else:
                i += 1
        return total

## Time Complexity: O(m + n)
## Space Complexity: O(1)