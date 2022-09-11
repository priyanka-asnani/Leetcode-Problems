class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        # build graph
        adjlist = [[] for _ in range(n)]
        for (src, dest) in connections:
            adjlist[src].append(dest)
            adjlist[dest].append(src)
            
        
        arrival = [0] * n
        lowest_arrival = [0] * n
        parent = [0] * n
        timestamp = 0
        visited = [-1] * n
        result = []
        
        def dfs(node):
            nonlocal timestamp
            timestamp += 1
            arrival[node] = timestamp
            visited[node] = 1
            lowest_arrival[node] = arrival[node]
            for neighbor in adjlist[node]:
                if visited[neighbor] == -1:
                    parent[neighbor] = node
                    neighbor_arrival = dfs(neighbor)
                    lowest_arrival[node]  = min(lowest_arrival[node], neighbor_arrival)
                # detect back edges
                elif neighbor != parent[node]:
                    lowest_arrival[node]  = min(lowest_arrival[node], arrival[neighbor])
            if arrival[node] == lowest_arrival[node] and node != 0:
                result.append([node, parent[node]])
            
            return lowest_arrival[node]
        
        dfs(0)
        return result
    
## Time complexity: O(M+N)
## Space complexity: O(M+N)
                    