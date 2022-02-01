# 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/

# Given an array of integers nums, sort the array in ascending order.

# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.helper(nums, 0, len(nums)-1)
        return nums
    
    def helper(self, nums, start, end):
        ## base case
        if start>= end:
            return
        else:
            ## implement lamoto's partioning
            # select random no 
            pindex = random.randint(start, end)
            ## swap pindex and start index
            temp_var = nums[pindex]
            nums[pindex] = nums[start]
            nums[start] = temp_var
            pivot = nums[start]
            less_than_pivot = start
            for i in range (start+1, end+1):
                if nums[i] < pivot:
                    less_than_pivot+=1 
                    temp = nums[i]
                    nums[i] = nums[less_than_pivot]
                    nums[less_than_pivot] = temp
            ## swap start value and last less_than_pivot pointer value
            temp_vars = nums[less_than_pivot]
            nums[less_than_pivot] = nums[start]
            nums[start] = temp_vars
            self.helper(nums, start, less_than_pivot-1)
            self.helper(nums, less_than_pivot+1, end)
            return