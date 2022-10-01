import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build a graph
        adjlist = [[] for _ in range(n)]
        for (src, dest) in edges:
            adjlist[src].append(dest)
            adjlist[dest].append(src)

        visited = [-1] * n
        # traverse graph using bfs
        def dfs(node):
            visited[node] = 1
            for neighbor in adjlist[node]:
                if visited[neighbor] == -1:
                    dfs(neighbor)
        
        # outer loop
        components = 0
        for v in range(len(visited)):
            if visited[v] == -1:
                components += 1
                dfs(v)

        return components

## Time Complexity: O(E + V)
## Space Complexity: O(E + V)