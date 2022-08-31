class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        left, max_length = 0, -1
        hashmap = {}
        for right in range(len(s)):
            # if character does not exists in hashmap
            if s[right] not in hashmap:
                hashmap[s[right]] = right
            # if charcter already exists in hashmap
            else:
                # compute the length of string
                old_index = hashmap[s[right]]
                str_len = right - old_index - 1
                # update the max length
                max_length = max(str_len, max_length)
                # slide the window
                left += 1
        return max_length
    
## Time complexity: O(N)
## Space complexity: O(1)