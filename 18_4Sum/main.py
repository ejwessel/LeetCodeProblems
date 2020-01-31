class Solution:

    def __init__(self):
        self.combinations = []
        self.SUM_SIZE = 4

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        self._fourSum(nums, target, [], 0)
        return self.combinations

    def _fourSum(self, nums, target, used_nums, intermittent_sum):
        if len(used_nums) > self.SUM_SIZE:
            return
        elif len(used_nums) == self.SUM_SIZE:
            if intermittent_sum == target:
                if used_nums not in self.combinations:
                    self.combinations.append(used_nums)
                return

        prev_num = None
        for i in range(len(nums)):
            # set prev_num
            if prev_num is None:
                prev_num = nums[i]
            else:
                # if we've already looked at this number in this iteration we can
                # skip over it since it will not provide any additional value
                if nums[i] == prev_num:
                    continue

            # set prev num since it will influence next loop
            prev_num = nums[i]
            selected_num = nums[i]
            self._fourSum(nums[i + 1:], target, used_nums + [selected_num], intermittent_sum + nums[i])


if __name__ == "__main__":
    output = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    expected = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
    for solution in expected:
        assert solution in output
    for solution in output:
        assert solution in expected

    output = Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
    expected = [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2],
                [-2, 0, 0, 2], [-1, 0, 0, 1]]
    for solution in expected:
        assert solution in output
    for solution in output:
        assert solution in expected

    output = Solution().fourSum([-5, 5, 4, -3, 0, 0, 4, -2], 4)
    expected = [[-5, 0, 4, 5], [-3, -2, 4, 5]]
    for solution in expected:
        assert solution in output
    for solution in output:
        assert solution in expected

    output = Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11)
    expected = [[-5, -4, -3, 1]]
    for solution in expected:
        assert solution in output
    for solution in output:
        assert solution in expected

    output = Solution().fourSum(
        [-493, -482, -482, -456, -427, -405, -392, -385, -351, -269, -259, -251, -235, -235, -202, -201, -194, -189,
         -187, -186, -180, -177, -175, -156, -150, -147, -140, -122, -112, -112, -105, -98, -49, -38, -35, -34, -18, 20,
         52, 53, 57, 76, 124, 126, 128, 132, 142, 147, 157, 180, 207, 227, 274, 296, 311, 334, 336, 337, 339, 349, 354,
         363, 372, 378, 383, 413, 431, 471, 474, 481, 492],
        6189
    )
