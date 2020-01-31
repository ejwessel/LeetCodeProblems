class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_idx = {}
        seen_nums = set()

        # populate num slots
        for i in range(len(nums)):
            num = nums[i]

            required_num = target - nums[i]

            # check if we've seen required before
            if required_num not in seen_nums:
                # if we havent then add it to our set
                if num not in seen_nums:
                    num_to_idx[num] = []
                    seen_nums.add(num)
                num_to_idx[num].append(i)
            else:
                # go through the indicies
                for j in num_to_idx[required_num]:
                    if i is j:
                        continue
                    return [i, j]

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

