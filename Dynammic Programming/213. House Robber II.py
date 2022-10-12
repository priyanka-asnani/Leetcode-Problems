class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        if len(nums) == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])

        n = len(nums)
        table = [0 for index in range(n)]

        # We neeed to somehow break the circle into a line
        # Case1: Suppose the first house, say house 0 was robbed
        # In this case, house n-1 couldn't be robbed and house 1 couldn't be robbed
        # We consult the best solution for houses 2...n-2 treating them as if they lie along a straight line
        table[2] = nums[2]
        table[3] = max(nums[2], nums[3])
        for i in range(4, n-1):
            table[i] = max(table[i-1], nums[i] + table[i-2])
        result1 = nums[0] + table[n-2]

        # Case2: Suppose the first house, say house 0 was not robbed
        # In this case, house n-1 couldn't be robbed 
        # We consult the best solution for houses 1...n-1 treating them as if they lie along a straight line
        table[1] = nums[1]
        table[2] = max(nums[1], nums[2])
        for j in range(3, n):
            table[j] = max(table[j-1], nums[j] + table[j-2])
        result2 = table[n-1]

        return max(result1, result2)

## Time Complexity: O(N)
## Space Complexity: O(N)