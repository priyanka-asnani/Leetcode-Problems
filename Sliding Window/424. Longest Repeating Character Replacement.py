class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        left, max_length = 0, 0
        for right in range(len(s)):
             # insert frequency of current character in hashmap
            if s[right] not in freq_map:
                freq_map[s[right]] = 0
            freq_map[s[right]] += 1
            window_len = right - left + 1
            max_freq = max(freq_map.values())
            if (window_len - max_freq) <= k:
                max_length = max(max_length, window_len)
            # if not a valid string
            if (window_len - max_freq) > k:
                # decrement the value of the element at left
                left_char = s[left]
                freq_map[left_char] -= 1
                if freq_map[left_char] == 0:
                    del freq_map[left_char]
                # slide the window and move the left pointer
                left += 1
        return max_length
    
## Time Complexity: O(N)
## Space Complexity: O(1)
            