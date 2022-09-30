import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build a graph
        adjlist = [[] for _ in range(n+1)]
        for (src, dest, weight) in times:
            adjlist[src].append((dest, weight))

        captured = [-1] * (n+1)
        num_captured = 0
        last_dist = 0
        q = [(0, k)]
        while q:
            (dist, node) = heapq.heappop(q)
            if captured[node] == -1:
               captured[node] = dist
               last_dist = dist
               num_captured += 1
               # look at all its neighbors
               for (neighbor, w) in adjlist[node]:
                   if captured[neighbor] == -1:
                       heapq.heappush(q, (captured[node] + w, neighbor))

        return last_dist if num_captured == n else -1

## Time Complexity: O(MlogN)
## Space Complexity: O(M+N) + O(m) 
            
