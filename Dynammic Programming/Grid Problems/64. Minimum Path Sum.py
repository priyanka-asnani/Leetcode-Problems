class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # fill the base case values for first row
        for row in range(1, m):
           grid[row][0] = grid[row][0] + grid[row-1][0]

        # fill the base case values for first column
        for col in range(1, n):
           grid[0][col] = grid[0][col] + grid[0][col-1]

        for rows in range(1, m):
            for cols in range(1, n):
                grid[rows][cols] = grid[rows][cols] + min(grid[rows-1][cols], grid[rows][cols-1])
        
        return grid[m-1][n-1]

## Time Complexity: O(M * N)
## Space Complexity: O(1)