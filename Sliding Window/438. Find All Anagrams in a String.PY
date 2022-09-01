from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        result = []
        hashmap = {}
        pattern_map = Counter(p)
        for right in range(len(s)):
            # insert element in hashmap
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] += 1
            window_len = right - left + 1
            if window_len == len(p):
                # check if current string is anagram of p
                if hashmap == pattern_map:
                    result.append(left)
                # slide the window
                # decrement the frequency of element at left
                left_char = s[left]
                hashmap[left_char] -= 1
                if hashmap[left_char] == 0:
                    del hashmap[left_char]
                # increment left pointer
                left += 1
        return result
    
## Time Complexity: O(M+N)
## Space Complexity: O(1)