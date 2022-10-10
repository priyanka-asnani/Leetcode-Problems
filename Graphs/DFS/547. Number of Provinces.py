class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [-1] * (n)

        # traverse the graph using DFS
        def dfs(node):
            visited[node] = 1
            for i, edge in enumerate(isConnected[node]):
                if visited[i] == -1 and edge == 1:
                    dfs(i)
        
        provinces = 0
        for x in range(len(isConnected)):
            if visited[x] == -1:
                provinces += 1
                dfs(x)
        return provinces
        

# Time Complexity: O(N)
# Space Complexity: O(N)