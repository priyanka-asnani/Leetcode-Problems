class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # matrix to store solutions to subproblems
        table = [[0] * n for i in range(m)]

        # check if starting cell has the obstacle
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            table[0][0] = 1

        # Fill in first row with 1's if no obstacle
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                break
            else:
               table[0][i] = 1 

        # Fill in first column with 1's if no obstacle
        for j in range(1, m):
            if obstacleGrid[j][0] == 1:
                break
            else:
               table[j][0] = 1

        # 
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                else: 
                    table[row][col] = table[row-1][col] +  table[row][col-1]

        # return value in the bottom right cell        
        return table[m-1][n-1]

## Time Complexity: O(M * N)
## Space Complexity: O(M * N)
        