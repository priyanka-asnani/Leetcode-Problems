class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        # set the initial pointer to bottom left value of the matrix
        r, c = n_rows - 1, 0
        while r >= 0 and c < n_cols:
            if target < matrix[r][c]:
                r -= 1
            elif target > matrix[r][c]:
                c += 1
            else:
                return True
        return False

## Time Complexity: O(M + N) 
## Space Complexity: O(1)