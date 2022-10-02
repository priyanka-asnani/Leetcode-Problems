class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbors(x, y):
            result = []
            if x+1 < len(grid):
                result.append((x+1, y))
            if y+1 < len(grid[0]):
                result.append((x, y+1))
            if x-1 >= 0:
                result.append((x-1, y))
            if y-1 >= 0:
                result.append((x, y-1))
            return result

        # traverse the grid using dfs
        def dfs(i, j):
            # mark the grid 0 when visited
            grid[i][j] = '0'
            neighbors = get_neighbors(i, j)
            for (neighbor_x, neighbor_y) in neighbors:
                if grid[neighbor_x][neighbor_y] != '0':
                    dfs(neighbor_x, neighbor_y)

        # outer loop
        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    dfs(x, y)
                    islands += 1
        return islands

## Time Complexity: O(M X N)
## Space Complexity: O(M X N)