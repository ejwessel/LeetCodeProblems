## Meeting Rooms 2

Runtime: O(n^2)
- sorting takes O(nlogn)
- linearly scan through sorted intervals
- for each interval scan an array of latest times
- worst case scenario there is no overlap and therefore latest times needs to be scanned for all elements

Space: O(n)
- worst case N non overlapping items need to be kept in the latest_times
- avg O(m when overlapped)