class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        start_index = self.startIndex(nums, target)
        print(start_index)
        end_index = self.endIndex(nums, target)
        print(end_index)
        nums_length = len(nums)//2
        integer_count = (end_index - start_index)+1
        count = 0 if start_index == -1 and end_index == -1 else integer_count
        if count > nums_length:
            return True
        
        
    def startIndex(self, nums, target):
        low = 0
        high = len(nums)-1
        index=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                index=mid
                high=mid-1
            elif nums[mid] < target:
                low = mid+1
            else:
                high=mid-1
        return index
    
    def endIndex(self, nums, target):
        low = 0
        high = len(nums)-1
        index=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                index=mid
                low=mid+1
            elif nums[mid] < target:
                low = mid+1
            else:
                high=mid-1
        return index

## Time Complexity: O(log N)
## Space Complexity: O(1)