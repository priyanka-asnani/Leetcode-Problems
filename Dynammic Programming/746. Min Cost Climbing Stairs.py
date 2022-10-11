class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        table = [0] * (n+2)
        table[1] = cost[0]
        length = len(table)
        cost.append(0)
        for i in range(2, length):
            table[i] = cost[i-1] + min(table[i-1], table[i-2])
        return table[-1]

## Time Complexity: O(N)
## Space Complexity: O(N)