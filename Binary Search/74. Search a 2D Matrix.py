class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_rows = len(matrix)
        n_cols = len(matrix[0])
        top_row, bot_row = 0, m_rows - 1
        while top_row <= bot_row:
            mid_row = top_row + (bot_row - top_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                break

        target_found = self.binarySearch(matrix[mid_row], target)
        if target_found:
            return True
        return False

    def binarySearch(self, row, target):
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True
                elif target > row[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

## Time Complexity: O(logM + logN)
## Space Complexity: O(1)