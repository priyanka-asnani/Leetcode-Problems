class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = []
        n = len(graph)
        
        def helper(node_id, slate):
            # base case
            if node_id == n-1:
                slate.append(node_id)
                paths.append(slate[:])
                slate.pop()
                return 
                
            # recursive case
            slate.append(node_id)
            for neighbor in graph[node_id]:
                helper(neighbor, slate)
            slate.pop()
            return
            
        helper(0, [])
        return paths
    
## Time Complexity: O(2^N * N)
## Space Complexity: O(N)