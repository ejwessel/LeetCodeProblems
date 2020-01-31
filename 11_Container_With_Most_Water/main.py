
class Solution1:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_known_area = 0;

        # go through all possible start container indicies
        for start_idx in range(0, len(height) - 1):
            # go through all possible end container indicies for a given start index
            for end_idx in range(start_idx + 1, len(height)):
                # compute x distance
                x_length = end_idx - start_idx
                y_min = min(height[start_idx], height[end_idx])
                area = x_length * y_min
                max_known_area = max(max_known_area, area)

        return max_known_area

class Solution2:
    def maxArea(self, height):
        """
          :type height: List[int]
          :rtype
        """

        max_known_area  = 0

        start_idx = 0
        end_idx = len(height) - 1

        while(start_idx < end_idx):
            y_height = min(height[start_idx], height[end_idx])
            x_length = end_idx - start_idx
            area = x_length * y_height
            max_known_area = max(max_known_area, area)

            # determine which boundary to shorten
            if height[start_idx] <= height[end_idx]:
                start_idx += 1
            else:
                end_idx -= 1

        return max_known_area

if __name__ == "__main__":

    max_area = Solution1().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(max_area)
    assert(max_area == 49)

    max_area = Solution2().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(max_area)
    assert(max_area == 49)
