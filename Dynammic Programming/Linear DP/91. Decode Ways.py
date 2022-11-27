class Solution:
    def numDecodings(self, s: str) -> int:
        # f(n) is the total number of ways to decode a string of length n
        n = len(s)
        table = [0] * (n+1)

        table[0] = 1
        table[1] = 1 if s[0] != '0' else 0

        for i in range(2, n+1):
            # table[i] is no of ways to decode chracters 0...i of string s
            if s[i-1] != '0': # if digit is not zero, then it could be encoded by itself
               table[i] += table[i-1]
            # OR if last two digits were encoded, then it can only happen if the previous digit was 1 or 2 and last digit was from 0..6 
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] in ['6', '5', '4', '3', '2', '1', '0']):
                table[i] += table[i-2]
        return table[-1]


## Time Complexity: O(N)
## Space Complexity: O(N)