class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key= lambda x: x[0])
        parent = [i for i in range(n)]
        size = [1] * n
        components = n
        for timestamp, u, v in logs:
            rootu = self.find(u, parent)
            rootv = self.find(v, parent)
            if rootu != rootv:
                if size[rootu] < size[rootv]:
                    parent[rootu] = rootv
                    size[rootv] += size[rootu]
                else:
                    parent[rootv] = rootu
                    size[rootu] += size[rootv]
                
                components -= 1
                if components == 1:
                    return timestamp
        return -1
    
    def find(self, x, parent):
        while x != parent[x]:
            x = parent[x]
        return x
    
        
    
## Time Complexity: O(N + MlogN)
## Space Complexity: O(N)