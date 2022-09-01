from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Sliding Window Approach
        left = 0
        hashmap = {}
        pattern_map = Counter(t)
        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] += 1
        # check if t is an anagram of s
        if hashmap == pattern_map:
            return True
        return False          
    
## Time Complexity: O(N)
## Space Complexity: O(1)