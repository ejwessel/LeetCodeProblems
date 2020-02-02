from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        merging intervals together
        :param intervals: the intervals to merge
        :return: the merged internals list
        '''
        i = 0

        # must sort first in order to have the list items be in the right order for merging
        intervals.sort()

        # -1 because we're looking +1 ahead
        while i < len(intervals) - 1:
            # reset merge for iteration
            merged = False
            a = intervals[i]
            b = intervals[i + 1]
            if a[0] <= b[0] <= a[1] and b[0] <= a[1] <= b[1]:
                intervals[i] = [a[0], b[1]]
                # remove the element that was merged
                intervals = intervals[:i + 1] + intervals[i + 2:]
                merged = True
            elif b[0] <= a[0] <= b[1] and a[0] <= b[1] <= a[1]:
                intervals[i] = [b[0], a[1]]
                # remove the element that was merged
                intervals = intervals[:i + 1] + intervals[i + 2:]
                merged = True
            elif a[0] <= b[0] <= b[1] <= a[1]:
                intervals[i] = [a[0], a[1]]
                intervals = intervals[:i + 1] + intervals[i + 2:]
                merged = True
            elif b[0] <= a[0] <= a[1] <= b[1]:
                intervals[i] = [b[0], b[1]]
                intervals = intervals[:i + 1] + intervals[i + 2:]
                merged = True

            # if we did not merge then we will iterate forward
            if not merged:
                i += 1

        return intervals


if __name__ == "__main__":
    sol = Solution()

    intervals = [[1, 4], [4, 5]]
    result = sol.merge(intervals)
    assert result == [[1, 5]]

    intervals = [[1, 3], [2, 6]]
    result = sol.merge(intervals)
    assert result == [[1, 6]]

    intervals = [[2, 5], [3, 6]]
    result = sol.merge(intervals)
    assert result == [[2, 6]]

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = sol.merge(intervals)
    assert result == [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 3], [2, 6], [8, 10], [9, 18]]
    result = sol.merge(intervals)
    assert result == [[1, 6], [8, 18]]

    intervals = [[1, 3], [2, 6], [3, 7], [8, 10], [9, 18]]
    result = sol.merge(intervals)
    assert result == [[1, 7], [8, 18]]

    intervals = [[1, 4], [0, 4]]
    result = sol.merge(intervals)
    assert result == [[0, 4]]

    intervals = [[1, 10], [4, 5]]
    result = sol.merge(intervals)
    assert result == [[1, 10]]

    # intervals are not in order
    intervals = [[4, 5], [1, 10]]
    result = sol.merge(intervals)
    assert result == [[1, 10]]

    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    result = sol.merge(intervals)
    assert result == [[1, 10]]

    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [-1, 10]]
    result = sol.merge(intervals)
    assert result == [[-1, 10]]

    intervals = [[2, 3], [4, 5], [6, 7], [8, 10], [1, 9], [2, 2]]
    intervals.sort()
    result = sol.merge(intervals)
    assert result == [[1, 10]]

