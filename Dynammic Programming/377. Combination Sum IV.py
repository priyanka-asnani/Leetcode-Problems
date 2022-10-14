class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        table = [0 for i in range(target+1)] # table[i] is total no of combinations amount to i
        table[0] = 1

        for i in range(1, target+1):
            for number in nums:
                if i-number >= 0:
                    table[i] += table[i-number]
        return table[-1]

## Time Complexity: O(N * T)
## Space Complexity: O(T)