from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        last_end = 0
        for interval in intervals:
            start, end = interval
            if start < last_end:
                return False
            last_end = end
        return True


if __name__ == "__main__":
    sol = Solution()
    result = sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
    assert not result

    result = sol.canAttendMeetings([[7, 10], [2, 4]])
    assert result
