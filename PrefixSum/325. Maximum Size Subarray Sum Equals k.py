class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        global_max = 0
        # given any value what is the smallest prefix adding upto that value
        hashmap = {0:0} # empty prefix has a length of zero
        # iterate over the nums array
        for i in range(len(nums)):
            # update the prefix_sum
            prefix_sum += nums[i]
            # find smallest length yellow prefix adding up to prefixsum - k
            if prefix_sum - k in hashmap:
                global_max = max(global_max, i+1 - hashmap[prefix_sum - k])
            # update hashmap
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i+1
        return global_max

## Time Complexity: O(N)
## Time Complexity: O(N)