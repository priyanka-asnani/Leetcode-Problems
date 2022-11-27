class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # imagine taking the interleaved string of s1 and s2 and pulling the characters from the two strings
        # visualize the alignment of two strings
        # there are only insertions and deletions and no matches or mismatches in the alignment
        # there is a combinotorial explosion in the number of such alignments
        # I will look at only the last character (a, _) or (_, a) to make the decision
        # The last character could have come from either s1 and s2
        # if last charcter matches s1, then f(i, j) =  f(i-1, j)
        # if last charcter matches s2, then f(i, j) =  f(i, j-1)
        # if either of the answer come back True, then my answer will also be True. otherwise it will be False
        # f(i, j) = (f(i-1, j) and s1[i-1] == s3[i+j-1]) OR (f(i, j-1) and s2[j-1] == s3[i+j-1])

        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)
        # create a matrix of length (m+1)(n+1)
        matrix = [[False] * (n+1) for _ in range(m+1)]
        # fill out the base case values for first row and first column
        matrix[0][0] = True

        for i in range(1, m+1):
            # if the current charcter matches the charcter in s3 and the prefix has been matched so far
            # # the prefix of s1 should exactly match prefix of s3
            if s1[i-1] == s3[i-1] and matrix[i-1][0]:
                matrix[i][0] = True 

        for j in range(1, n+1):
            # the prefix of s2 should exactly match prefix of s3
            if s2[j-1] == s3[j-1] and matrix[0][j-1]:
                matrix[0][j] = True 

        # fill out the internal values iin the matrix
        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix[i][j] = (s1[i-1] == s3[i+j-1] and matrix[i-1][j]) or (s2[j-1] == s3[i+j-1] and matrix[i][j-1])
        
        return matrix[-1][-1]

## Time Complexity: O(M*N)
## Space Complexity: O(M*N)