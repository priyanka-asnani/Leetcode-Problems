class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_excess = 0
        # given any excess value what is the smallest subarray having it
        hashmap = {0:0} # empty prefix has a length of zero
        global_max = 0
        # iterate over the nums array
        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_excess += 1
            else:
                prefix_excess -= 1 
            if prefix_excess in hashmap:      
                global_max = max(global_max, i+1 - hashmap[prefix_excess])
             # update hashmap
            if prefix_excess not in hashmap:
                 hashmap[prefix_excess] = i+1
        return global_max

## Time Complexity: O(N)
## Space Complexity: O(N)