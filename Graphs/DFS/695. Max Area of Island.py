class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        # function to get neigbors
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
        
        # traverse the graph using DFS
        def dfs(i, j):
            # mark grid as '0' when visited
            grid[i][j] = 0
            neighbors = get_neighbors(i, j)
            result = 1
            for (neighbor_x, neighbor_y) in neighbors:
                # if neighbor is not visited
                if grid[neighbor_x][neighbor_y] == 1:
                    result += dfs(neighbor_x, neighbor_y)
            return result

        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y] == 1):
                    max_area = max(max_area, dfs(x, y))
        return max_area

## Time Complexity: O(M x N)
## Space Complexity: O(M x N)
