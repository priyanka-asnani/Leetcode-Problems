# 744. Find Smallest Letter Greater Than Target

# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

# Note that the letters wrap around.

# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Example 2:

# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Example 3:

# Input: letters = ["c","f","j"], target = "j"
# Output: "j"

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
