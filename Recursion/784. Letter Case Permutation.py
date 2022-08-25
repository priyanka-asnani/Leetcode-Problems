class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ## using recursion
        result = []
        def helper(s, i, slate):
            # base case
            if i == len(s):
                # add the result to global bag
                result.append(''.join(slate[:]))
                return
            # recursive case
            # check if the character is a letter
            else:
                if s[i].isalpha():
                    slate.append(s[i].lower())
                    helper(s, i+1,  slate)
                    slate.pop()
                    slate.append(s[i].upper())
                    helper(s, i+1,  slate)
                    slate.pop()
                # check if the character is a digit
                else:
                    slate.append(s[i])
                    helper(s, i+1,  slate)
                    slate.pop()  
                return
        helper(s, 0, [])
        return result
    
## Time complexity: O(2^N * N)
## Space complexity: O(2^N * N)
        