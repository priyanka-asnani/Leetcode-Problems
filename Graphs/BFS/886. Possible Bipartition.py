import collections
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # build a graph
        adjlist = [[] for _ in range(n+1)]
        for (src, dest) in dislikes:
           adjlist[src].append(dest)
           adjlist[dest].append(src) 

        visited = [-1] * (n+1)
        parent = [-1] * (n+1)
        distance = [-1] * (n+1)
        
        # traverse the graph using BFS
        def bfs(source):
            visited[source] = 1
            distance[source] = 0
            q = collections.deque([source])
            while q:
                node = q.popleft()
                for neighbor in adjlist[node]:
                # if node is not visited
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        parent[neighbor] = node
                        distance[neighbor] =  distance[node] + 1
                        q.append(neighbor)
                    # neighbor is already visited
                    else:
                    # detect cross-edge
                        if neighbor != parent[node]:
                            # if the vertices are on the same level
                            if distance[neighbor] == distance[node]:
                                return False
            return True
        
        # outer loop
        for v in range(n+1):
            if visited[v] == -1:
                if bfs(v) == False:
                    return False
        return True

## Time Complexity: O(E + V)
## Space Complexity: O(E + V)