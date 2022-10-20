class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        self.prefix_sum.append(0)
        for i in range(len(nums)):
            sum = nums[i] + self.prefix_sum[i]
            self.prefix_sum.append(sum)   

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


## Time Complexity: O(1)
## Space Complexity: O(N)