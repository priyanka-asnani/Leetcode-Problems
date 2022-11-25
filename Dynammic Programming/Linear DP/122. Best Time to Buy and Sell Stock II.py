class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # gtable[i] is the max profit wih any number of transactions upto index i
            # gtable[i] = max(gtable[i-1], ftable[i])
        # ftable[i] is the max profit with any number of transactions upto index i with sell happening on day i
            # if purchase date is previous day then profit is prices[i] - prices[i-1] + (gtable[i-1])
            # if purchase date is earlier day then max profit is prices[i] - prices[i-1] + ftable[i-1] (max profit with any # transactions ending at i-1 and selling on day i-1)
        
        n = len(prices)
        ftable = [0] * n
        gtable = [0] * n

        for i in range(1, n):
            ftable[i] = max(prices[i] - prices[i-1] + gtable[i-1], ftable[i-1] + prices[i] - prices[i-1])
            gtable[i] = max(gtable[i-1], ftable[i])
        return gtable[-1]

## Time Complexity: O(N)
## Space Complexity: O(N)