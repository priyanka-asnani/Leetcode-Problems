class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                # compute mahattan distance
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, distance))

       # sorting edges by distance
        edges.sort(key= lambda x:x[2])
        parent = [i for i in range(n)]
        size = [1] * n
        total_cost = 0
        components = n

       # iterate over all edges
        for u, v, cost in edges:
           rootu = self.find(u, parent)
           rootv = self.find(v, parent)

           if rootu != rootv:
               if size[rootu] < size[rootv]:
                   # make rootv as the parent
                   parent[rootu] = rootv
                   size[rootv] += size[rootu]

               else:
                    # make rootu as the parent
                   parent[rootv] = rootu
                   size[rootu] += size[rootv]
               total_cost += cost
               components -= 1
               if components == 1: 
                   return total_cost
        return 0

    def find(self, x, parent):
        while x != parent[x]:
            x = parent[x]
        return x

## Time Complexity: O(N^2)
## Space Complexity: O(N)

