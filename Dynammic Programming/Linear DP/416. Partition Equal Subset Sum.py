class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # to partition the the array into subsets of equal sum, the total must be even
        if total % 2 != 0:
            return False
        
        # we are searching for subset half the total sum
        # find the subset where sum is equal to k
        k = total // 2
        n = len(nums)

        # here each element can be included or excluded from the subset
        # I will only make the decision for the last number
        # If I exclude the last number, then is there is a subset from previous n-1 numbers adding upto k
        # If I include the last number, then is there is a subset from previous n-1 numbers adding upto k - last number
        # if either of the answer is True, my answer will be a True
        # f(n, k) = f(n-1, k) or f(n-1, k-value of nth number)

        # create a (n+1)(k+1) matrix
        matrix = [[True] * (k+1) for _ in range(n+1)]

        # fill in the base case values
        matrix[0][0] = True

        # f(0, k) = False because we cannot get a get a subset sum of non-zero by including zero elements
        for target in range(1, k+1):
            matrix[0][target] = False

        # f(n, 0) = True because we can exclude the elements to get a subset sum of zero
        for row in range(1, n+1):
            matrix[row][0] = True

        # filling in the table
        for row in range(1, n+1):
            for target in range(1, k+1):
                matrix[row][target] = matrix[row-1][target]
                if target >= nums[row-1]:
                    matrix[row][target] = (matrix[row-1][target]) or (matrix[row-1][target - nums[row-1]])

        return matrix[-1][-1]

## Time Complexity: O(N*K)
## Space Complexity: O(N*K)