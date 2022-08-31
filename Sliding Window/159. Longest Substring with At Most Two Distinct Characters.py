class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, max_length = 0, 0
        hashmap = {}
        # iterate over the string
        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] += 1
            # compute the length of string
            window_length = right - left + 1
            if len(hashmap) <= 2:
                max_length = max(max_length, window_length)
            if len(hashmap) > 2:
                # move the sliding window
                left_char = s[left]
                hashmap[left_char] -= 1
                if hashmap[left_char] == 0:
                    del hashmap[left_char]
                left += 1
        return max_length
    
## Time Complexity: O(N)
## Space Complexity: O(1)