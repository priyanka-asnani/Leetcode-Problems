class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # using Recursion & Backtracking
        result = []
        def helper(left, right, slate):
            # backtracking case
            if left > right:
                return
            
            # base case
            if left == 0 and right == 0:
                result.append(''.join(slate))
                return
            
            # recursive case
            if left > 0:
                slate.append("(")
                helper(left-1, right, slate)
                slate.pop()
            if right > 0:
                slate.append(")")
                helper(left, right-1, slate)
                slate.pop()
            return
        helper(n, n, [])
        return result
    
## Time Complexity: O(2^2N * N)
## Space Complexity: O(2^2N * N)