class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # we need to divide the set into two subsets such that their difference is equal to target
        # one subset will comprise of all positive values and the other subset will comprise of all negative values
        # 
        # count the number of subsets with target k
        # this problem has now reduced to count subsets problem

        # count the number of zeroes in nums array
        zeros = nums.count(0)

        # removing all 0's from the nums array
        nums = [element for element in nums if element != 0]

        # if (target + sum(nums)) is odd, then we cannot make any subsets 
        target = abs(target)
        if (target + sum(nums)) % 2: return 0

        if target > sum(nums): return 0

        k = (target + sum(nums)) // 2
        n = len(nums)

        matrix = [[0] * (k+1) for _ in range(n+1)]

        # fill in the base case values
        matrix[0][0] = 1

        for row in range(1, n+1):
            matrix[row][0] = 1

        for col in range(1, k+1):
            matrix[0][col] = 0

        for row in range(1, n+1):
            for s in range(1, k+1):
                # if exclude the last number, f(n, target) = f(n-1, target)
                matrix[row][s] = matrix[row-1][s]
                if s >= nums[row-1]:
                    # if include the last number, f(n, target) = f(n-1, target) + f(n-1, target - last number)
                    matrix[row][s] = matrix[row-1][s] + matrix[row-1][s-nums[row-1]]
        return matrix[-1][-1]*pow(2,zeros)


## Time complexity: O(N * K)
## Space complexity: O(N * K)
