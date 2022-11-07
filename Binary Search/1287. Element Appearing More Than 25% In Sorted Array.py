class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count, result = 0, 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                count += 1
                if count > len(arr) // 4:
                    return arr[i]
            else:
                count = 1
        return arr[0]
                

## Time complexity: 0(N)
## Space complexity: 0(1)