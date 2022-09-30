import math
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # build a graph
        adjlist = [[] for _ in range(n)]
        for i in range(len(edges)):
            (src, dest) = edges[i]
            adjlist[src].append((dest, -math.log(succProb[i])))
            adjlist[dest].append((src, -math.log(succProb[i])))

        captured = [-1] * n
        q = [(0, start)]
        while q:
            (dist, node) = heapq.heappop(q)
            if captured[node] == -1:
                captured[node] = dist
                if node == end:
                    return math.exp(-captured[node])
                # traverse all its neighbors
                for (neighbor, w) in adjlist[node]:
                    if captured[neighbor] == -1:
                        # insert neighbor in heap
                        heapq.heappush(q, (captured[node] + w, neighbor))
        return 0

## Time Complexity: O(MlogN)
## Space Complexity: O(M+N) + O(M)