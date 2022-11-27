class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        table = [0] * n

        # base case: if it was 1-day travelling plan, then we choose the cheapest of three passes
        table[0] = min(costs)

        for i in range(1, n):
            # table[i] is the min cost for travel from days[0..i]
            # days[i] can be covered by 1-day/7-day/30-day pass

            # if day[i] is covered by 1-day pass
            case1 = table[i-1] + costs[0]

            # if day i is covered by 7-day pass, then we assume the 6 previous day are also covered by 7-day pass
            j = i - 1
            while j>=0 and days[j] >= days[i] - 6:
                j = j - 1

            if j >= 0:
              case2 = table[j] + costs[1]
            else:
                case2 = costs[1]

            # if day i is covered by 30-day pass, then we assume the 29 previous day are also covered by 30-day pass
            j = i - 1
            while j>=0 and days[j] >= days[i] - 29:
                j = j - 1

            if j >= 0:
              case3 = table[j] + costs[2]
            else:
                case3 = costs[2] 
            
            table[i] = min(case1, case2, case3)

        return table[-1]

## Time Complexity: O(N)
## Space Complexity: O(N)