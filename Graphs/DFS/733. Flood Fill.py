class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color_to_be_replaced = image[sr][sc]
        # function to get neighbors
        def get_neighbors(x, y):
            result = []
            if x+1 < len(image):
                result.append((x+1, y))
            if y+1 < len(image[0]):
                result.append((x, y+1))
            if x-1 >= 0:
                result.append((x-1, y))
            if y-1 >= 0:
                result.append((x, y-1))
            return result

        def dfs(i, j):
            # mark the grid with new color if visited
            image[i][j] = -1
            neighbors = get_neighbors(i, j)
            for (neighbor_x, neighbor_y) in neighbors:
                # neighbor not visited
                if image[neighbor_x][neighbor_y] == color_to_be_replaced:
                    dfs(neighbor_x, neighbor_y)

        dfs(sr, sc)
        for x in range(len(image)):
            for y in range(len(image[0])):
                if image[x][y] == -1:
                    image[x][y] = color
        return image

## Time Complexity: O(N)
## Space Complexity: O(N)