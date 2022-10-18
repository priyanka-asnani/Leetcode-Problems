class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high=len(letters)-1
        letter=letters[0]
        while low<=high:
            mid=(low+high)//2
            if target >= letters[mid]:
                low=mid+1
            else: 
                letter = letters[mid]
                high=mid-1
        return letter


## Time Complexity: O(log N)
## Space Complexity: O(1)