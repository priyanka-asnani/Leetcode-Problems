class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build a graph
        adjlist = [[] for _ in range(n)]
        for (src, dest) in edges:
           adjlist[src].append(dest) 
           adjlist[dest].append(src)

        visited = [-1] * n
        parent = [-1] * n

        # traverse the graph using dfs
        def dfs(node):
           visited[node] = 1
           for neighbor in adjlist[node]:
               if visited[neighbor] == -1:
                   parent[neighbor] = node
                   if dfs(neighbor): return True
               # neigbor has been visited
               else:
                   # presence of back edge, cycle detected
                   if neighbor != parent[node]: return True
         # cycle not found
           return False                 

        # outer loop
        components = 0
        for v in range(len(visited)):
            if visited[v] == -1:
                components += 1
                # if more than one component, then graph is not a tree
                if components > 1: return False
                # cycle found, hence graph is not a tree
                if dfs(v): return False
        return True

## Time Complexity: O(E + V)
## Space Complexity: O(E + V)
