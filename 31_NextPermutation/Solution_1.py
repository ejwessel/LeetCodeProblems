class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for [n-1, 0]; count backwards
        for i in range(len(nums) - 2, -1, -1):
            nums_to_right = nums[i + 1:]
            next_best_idx = self.next_best(nums[i], nums_to_right)
            # update index to nums's index only if valid idx
            if next_best_idx > -1:
                next_best_idx += (i + 1)

            # if min to right is greater than current we can get next lex num
            if next_best_idx > 0:
                self.swap_indices(nums, i, next_best_idx)

                # handle misordering on right side
                right_nums = nums[i + 1:]
                right_nums.sort()
                new_nums = nums[:i + 1] + right_nums

                # update original nums
                for j in range(len(new_nums)):
                    nums[j] = new_nums[j]
                return

        nums.sort()

    def next_best(self, current_num, right_list):
        best_i = -1
        for i in range(len(right_list)):
            if right_list[i] > current_num:
                # if best has not been set
                if best_i == -1 :
                    best_i = i
                # compare best i
                elif right_list[i] < right_list[best_i]:
                    best_i = i
        return best_i

    def swap_indices(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

if __name__ == "__main__":
    sol = Solution()
    # list = [1, 2, 3, 4]
    list = [5, 2, 5, 1]
    seen_list = []
    print(list)
    for i in range(25):
        sol.nextPermutation(list)
        print(list)

    # sol = Solution().nextPermutation([1])
    # sol = Solution().nextPermutation([1, 2])
    # sol = Solution().nextPermutation([1, 2, 3])
    # sol = Solution().nextPermutation([3, 2, 1])
    # sol = Solution().nextPermutation([1, 1, 5])
    # sol = Solution().nextPermutation([1, 3, 2])  # [2, 1, 3]
    # sol = Solution().nextPermutation([2, 3, 1])  # [3, 2, 1]
    # sol = Solution().nextPermutation([[5, 4, 7, 5, 3, 2]])  # [5, 5, 2, 3, 4, 7]
