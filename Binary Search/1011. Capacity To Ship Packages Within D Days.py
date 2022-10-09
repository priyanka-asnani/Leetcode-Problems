class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.calculateShipmentDays(weights, mid, days):
                right = mid
            else:
                left = mid + 1
        return right

    def calculateShipmentDays(self, weights, capacity, days):
        total_weight, days_taken = 0, 1
        for j in range(len(weights)):
            total_weight += weights[j]
            if total_weight > capacity:
                days_taken += 1
                total_weight = weights[j]
        return days_taken <= days


## Time Complexity: O(N log N)
## Space Complexity: O(1)
