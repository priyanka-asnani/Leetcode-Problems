class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a graph
        adjlist = [[] for _ in range(numCourses)]
        for (src, dest) in prerequisites:
            adjlist[dest].append(src)

        visited = [-1] * numCourses
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]

        def dfs(node):
            timestamp[0] += 1
            arrival[node] =  timestamp[0]
            visited[node] = 1
            for neighbor in adjlist[node]:
                if visited[neighbor] == -1:
                    if dfs(neighbor):
                        return True 
                else:
                    if departure[neighbor] == -1:
                        # back edge exists indicating a cycle
                        return True
            timestamp[0] += 1
            departure[node] =  timestamp[0]
            return False

        for v in range(numCourses):
            if visited[v] == -1:
                # if cycle found, we cannot complete courses
                if dfs(v):
                    return False
            # no cycle found, hence we camplete all courses
        return True

## Time Complexity: O(E + V)
## Space Complexity: O(E + V)