class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # f(i) = Boolean answer to the question "can c1c2..ci  be segmented in a valid way"
        # if ci is valid, then f(i-1)
        # if ci-1ci is valid, then f(i-2)
        # if ci-2ci-1ci is valid, then f(i-3)
        # of c1..ci is valid, then f(0) empty string

        n = len(s)
        word_dict = set(wordDict)
        table = [False for i in range(n+1)]
        # define base case
        table[0] = True

        # use topological sort order to populate the values
        for i in range(1, n+1):
            for lastwordlen in range(0, i):
                # if the substring in the dictionary
                if s[lastwordlen:i] in word_dict and table[lastwordlen] == True:
                    table[i] = True
        return table[-1]

## Time Complexity: O(N^2)
## Space Complexity: O(N)