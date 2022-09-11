class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        ## Kruskal Algorithm
        # sort all edges by theur weight
        connections.sort(key= lambda x:x[2])
        parent = [i for i in range(0, n+1)]
        size = [1] * (n+1)
        components = n
        total_cost = 0
        # iterate over all edges
        for u, v, cost in connections:
            uroot = self.find(u, parent)
            vroot = self.find(v, parent)
            if uroot != vroot:
                # check if size of parent of u is less than size of parent of v
                if size[uroot] < size[vroot]:
                    # make vroot as the parent of uroot
                    parent[uroot] = vroot
                    # increase the size of vroot
                    size[vroot] += size[uroot]
                
                else:
                    # make uroot as the parent of vroot
                    parent[vroot] = uroot
                    # increase the size of uroot
                    size[uroot] += size[vroot]
                    
                components -= 1
                total_cost += cost
                if components == 1:
                    return total_cost
        return -1
    
    def find(self, x, parent):
        while x != parent[x]:
            x = parent[x]
        return x
    
## Time Complexity: O(N + MlogN)
## Space Complexity: O(N)