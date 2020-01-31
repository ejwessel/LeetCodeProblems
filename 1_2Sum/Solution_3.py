class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        req_to_idx = {}

        # populate num slots
        for i in range(len(nums)):
            required_num = target - nums[i]

            # check for solution look up
            if req_to_idx.get(required_num) is not None:
                return [i, req_to_idx[required_num]]

            # if not then save idx
            req_to_idx[nums[i]] = i


if __name__ == "__main__":
    sol = Solution().twoSum([2, 7, 11, 15], 9)
    sol.sort()
    print(sol)
    assert sol == [0, 1]

    sol = Solution().twoSum([3, 2, 4], 6)
    sol.sort()
    print(sol)
    assert sol == [1, 2]

    sol = Solution().twoSum([2, 7, 11, 15, 2], 4)
    sol.sort()
    print(sol)

