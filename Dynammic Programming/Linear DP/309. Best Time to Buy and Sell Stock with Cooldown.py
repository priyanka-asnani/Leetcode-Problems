class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # gtable[i] is max profit from any number of transactions upto index i
        # ftable[i] is max profit from any number of transactions upto index i and sell at i
            # if buy happend on previous day, then ftable[i] = p[i] - p[i-1] + gtable[i-3]
            # if buy happened on earlier day, then ftable[i] = p[i] - p[i-1] + ftable[i-1]

        n = len(prices)
        ftable = [0] * n
        gtable = [0] * n
        
        for i in range(1, n):
            ftable[i] = max(prices[i] - prices[i-1] + gtable[i-3], prices[i] - prices[i-1] + ftable[i-1])
            gtable[i] = max(gtable[i-1], ftable[i])
        return gtable[-1]


## Time Complexity: O(N)
## Space Complexity: O(N)