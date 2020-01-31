class Solution:

    def __init__(self):
        self.k_sums = {}

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        self.k_sums[target] = []
        self.find_k_sum(nums, [], target, 0, 0, 4)
        return self.k_sums[target]

    def find_k_sum(self, remaining_nums, used_nums, target, intermittent_sum, current_depth, max_depth):

        # stop one before the max length
        if current_depth == max_depth - 1:
            required_num = target - intermittent_sum

            # I have all k_lengths - 1, look for a required value in the remaining numbers
            if required_num in remaining_nums:
                self.k_sums[target].append(used_nums + [required_num])
            return

        seen_nums = set()
        for i in range(len(remaining_nums)):
            if remaining_nums[i] in seen_nums:
                continue
            seen_nums.add(remaining_nums[i])

            self.find_k_sum(remaining_nums[i + 1:], used_nums + [remaining_nums[i]], target,
                            intermittent_sum + remaining_nums[i], current_depth + 1,
                            max_depth)


if __name__ == "__main__":
    '''
    output = Solution()
    input = [1, 0, -1, 0, -2, 2]
    input.sort()
    output.find_k_sum(input, [], 0, 0, 0, 2)
    print(output.k_sums)

    output = Solution()
    input = [-3, -2, -1, 0, 0, 1, 2, 3]
    input.sort()
    output.find_k_sum(input, [], 0, 0, 0, 2)
    print(input)
    print(output.k_sums)

    output = Solution()
    input = [-3, -2, -1, 0, 0, 1, 2, 3]
    input.sort()
    output.find_k_sum(input, [], 0, 0, 0, 3)
    print(output.k_sums)

    output = Solution()
    input = [-3, -2, -1, 0, 0, 1, 2, 3]
    input.sort()
    output.find_k_sum(input, [], 2, 0, 0, 3)
    print(output.k_sums)
    '''

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
    expected = []
    for solution in expected:
        assert solution in output
    for solution in output:
        assert solution in expected

    output = Solution().fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -9)
    expected = [[-5, -4, -1, 1], [-5, -4, 0, 0], [-5, -2, -2, 0], [-4, -2, -2, -1]]
    for solution in expected:
        assert solution in output
    for solution in output:
        assert solution in expected

    output = Solution().fourSum(
        [-497, -481, -481, -472, -471, -465, -422, -420, -413, -405, -388, -381, -366, -361, -359, -348, -334, -334,
         -318, -310, -305, -280, -273, -272, -262, -254, -248, -223, -208, -202, -196, -192, -189, -167, -165, -165,
         -156, -143, -136, -122, -120, -120, -108, -77, -50, -44, -34, -26, -17, -5, 13, 46, 46, 53, 54, 56, 66, 71, 72,
         75, 89, 115, 130, 139, 149, 151, 154, 196, 209, 219, 230, 240, 245, 246, 253, 267, 277, 289, 299, 302, 303,
         304, 342, 349, 360, 361, 361, 375, 392, 400, 407, 408, 408, 426, 427, 429, 443, 451, 481],
        -5617)
    expected = []
    for solution in expected:
        assert solution in output
    for solution in output:
        assert solution in expected
