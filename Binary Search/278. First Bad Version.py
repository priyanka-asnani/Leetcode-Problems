# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=0
        high=n-1
        bad_version = 0
        while low<=high:
            mid=(low+high)//2
            value = isBadVersion(mid+1)
            if value == True:
                bad_version = mid+1
                high=mid-1
            else:
                low=mid+1
        return bad_version

## Time Complexity: O(log N)
## Time Complexity: O(1)