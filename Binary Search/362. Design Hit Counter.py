class HitCounter:

    def __init__(self):
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300
        left, right = 0, len(self.hits) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.hits[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return len(self.hits) - left

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

## Time Complexity: O(log N)
## Space Complexity: O(1)