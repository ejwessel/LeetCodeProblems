from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        latest_times = []
        intervals.sort()
        for interval in intervals:
            start, end = interval
            added = False
            for i in range(len(latest_times)):
                if latest_times[i] <= start:
                    latest_times[i] = end
                    added = True
                    break
            if not added:
                latest_times.append(end)
        return len(latest_times)


if __name__ == "__main__":
    sol = Solution()
    result = sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
    assert result == 2

    result = sol.minMeetingRooms([[7, 10], [2, 4]])
    assert result == 1

    result = sol.minMeetingRooms([[11, 20], [20, 30], [25, 30], [5, 15], [8, 11]])
    assert result == 2

    result = sol.minMeetingRooms([[10, 20], [20, 30], [25, 30], [5, 15], [8, 11]])
    assert result == 3
