class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ## Sliding Window Approach
        left = 0
        max_length = 0
        freq_map = {}
        # iterate over the string
        for right in range(len(s)):
            if s[right] not in freq_map:
                freq_map[s[right]] = 0
            freq_map[s[right]] += 1
            # track max length
            length = right - left + 1
            if len(freq_map) <= k:
                 max_length = max(length , max_length)   
            while len(freq_map) > k:
                # decrement the value of charcter in hashmap
                left_char = s[left]
                freq_map[left_char] -= 1
                if freq_map[left_char] == 0:
                    del freq_map[left_char]
                left += 1
        return max_length

## Time Complexity: O(N)
## Space Complexity: O(k)