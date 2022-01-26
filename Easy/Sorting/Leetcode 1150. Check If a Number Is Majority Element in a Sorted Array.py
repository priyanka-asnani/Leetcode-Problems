# 1150. Check If a Number Is Majority Element in a Sorted Array

# Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.

# A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

 

# Example 1:

# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
# Output: true
# Explanation: The value 5 appears 5 times and the length of the array is 9.
# Thus, 5 is a majority element because 5 > 9/2 is true.
# Example 2:

# Input: nums = [10,100,101,101], target = 101
# Output: false
# Explanation: The value 101 appears 2 times and the length of the array is 4.
# Thus, 101 is not a majority element because 2 > 4/2 is false.

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
        