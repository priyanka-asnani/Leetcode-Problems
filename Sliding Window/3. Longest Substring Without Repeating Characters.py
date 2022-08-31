class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window Approach
        left, max_length = 0, 0
        hashset = set()
        for right in range(len(s)):
            # encounter a duplicate character
            while s[right] in hashset:
                # slide the window
                # remove character at the left pointer from hashset
                hashset.remove(s[left])
                # remove the left pointer by 1
                left += 1
                # add the current charcter to hashset
            hashset.add(s[right])
            # compute length of string
            str_len = right - left + 1
            #update max length
            max_length = max(max_length, str_len)
        return max_length

    
## Time Complexity: O(N)
## Space Complexity: O(N)