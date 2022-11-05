class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore algorithm
        result, count = 0, 0
        for num in nums:
            if count == 0:
                result = num
            count += (1 if num == result else -1)
        return result


        """
        Hash-map approach
        hashmap = {}
        result, max_count = 0, 0
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
            count = hashmap[num]
            result = num if count > max_count else result
            # update the max count
            max_count = max(max_count, count)
        return result
        """

## Time Complexity: O(N)
## Space Complexity: O(1)