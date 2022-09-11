import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## creating the adjacency list
        adjlist = [[] for _ in range(n)]
        for (src, dest) in edges:
            adjlist[src].append(dest)
            adjlist[dest].append(src)
            
        visited = [-1]*n
        ## breadth first search function
        def bfs(source):
            queue = collections.deque()
            queue.append(source)
            visited[source] = 1
            while queue:
                node = queue.popleft()
                for neighbor in adjlist[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        queue.append(neighbor)
                            
        components = 0
        for i in range(len(visited)):
            if visited[i] == -1:
                components+=1
                bfs(i)
        return components

## Time Complexity: O(M+N)
## Space Complexity: O(M+N)
                