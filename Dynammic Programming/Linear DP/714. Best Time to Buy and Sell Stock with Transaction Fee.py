class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        ftable = [0] * n
        gtable = [0] * n

        ftable[0] = -fee
        
        for i in range(1, n):
            ftable[i] = max(prices[i] - prices[i-1] - fee + gtable[i-1], prices[i] - prices[i-1] + ftable[i-1])
            gtable[i] = max(gtable[i-1], ftable[i])
        return gtable[-1]


## Time Complexity: O(N)
## Space Complexity: O(N)