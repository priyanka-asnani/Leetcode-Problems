from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        pattern_map = Counter(s1)
        left = 0
        for right in range(len(s2)):
            if s2[right] not in hashmap:
                hashmap[s2[right]] = 0
            hashmap[s2[right]] += 1
            window_len = right - left + 1
            if window_len == len(s1):
                # check if current window matches the pattern s1
                if hashmap == pattern_map:
                    return True
                else:
                    # derement the value of character at the left pointer 
                    hashmap[s2[left]] -= 1
                    if hashmap[s2[left]] == 0:
                        del hashmap[s2[left]]
                    # slide the window to the right
                    left += 1
        return False

## Time Complexity: O(N)
## Space Complexity: O(1)
            