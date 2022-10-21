class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## Hashmap Approach
        # create hashmap to keep track of prefix sum and its frequency
        prefix_sum = 0
        count = 0
        hashmap = {0:1}
        # iterate over the nums array
        for i in range(len(nums)):
            # update the prefix_sum
            prefix_sum += nums[i] 
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = 1
            else:
                hashmap[prefix_sum] += 1
        return count
    
## Time Complexity: 0(N)
## Space Complexity: 0(N)