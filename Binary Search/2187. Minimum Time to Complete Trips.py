class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = totalTrips * min(time)
        min_time = float(inf)
        while left <= right:
            mid = left + (right - left) // 2
            expected_trips = self.findTrips(mid, time, totalTrips)
            if expected_trips >= totalTrips:
                min_time = min(min_time, mid)
                right = mid-1
            else:
                left = mid + 1
        return min_time

    def findTrips(self, trip_time, times, total_trips):
        expected_trips = 0
        for time in times:
            quotient = trip_time // time
            expected_trips += quotient
        return expected_trips

## Time Complexity: O(N log M)
## Space Complexity: O(1)