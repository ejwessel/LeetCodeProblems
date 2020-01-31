import sys

print_debug = True

class Solution:

    def getCloserSum(self, sum_to_compare, known_closest_sum, target):
        if abs(known_closest_sum - target) > abs(sum_to_compare - target):
            return sum_to_compare
        else:
            return known_closest_sum

    def threeSumClosestHelper(self, a, b, left_bound, right_bound, nums, target, known_closest_sum):

        if print_debug: print("------------------------")

        if b == left_bound and b == right_bound:
            if print_debug: print("left_bound, b, right_bound equal")
            if print_debug: print('known_closest_sum: {} to target {}'.format(known_closest_sum, target))
            return known_closest_sum

        # compute c1
        c1 = int((left_bound + b) / 2)
        # compute c2
        c2 = int((b + right_bound) / 2)

        dist1 = sys.maxsize
        dist2 = sys.maxsize

        if c1 <= left_bound or c1 == b:
            pass
        else:
            sum1 = nums[a] + nums[b] + nums[c1]
            if print_debug: print("a:{} b:{} c1:{}".format(a, b, c1))
            if print_debug: print([nums[a], nums[b], nums[c1]])
            if print_debug: print("sum1 = {}".format(sum1))
            dist1 = abs(sum1 - target)
            if print_debug: print("dist1 = {}".format(dist1))

        if c2 >= right_bound or c2 == b:
            pass
        else:
            sum2 = nums[a] + nums[b] + nums[c2]
            if print_debug: print("a:{} b:{} c2:{}".format(a, b, c2))
            if print_debug: print([nums[a], nums[b], nums[c2]])
            if print_debug: print("sum2 = {}".format(sum2))
            dist2 = abs(sum2 - target)
            if print_debug: print("dist2 = {}".format(dist2))


        if dist1 == sys.maxsize and dist2 == sys.maxsize:
            if print_debug: print("no dist1 and no dist2, moving forward")
            return self.threeSumClosestHelper(a, b, b, b, nums, target, known_closest_sum)

        elif dist1 == dist2:
            if print_debug: print('dist1 equals dist2, check both paths')
            # if distances are the same then c1 == b == c2
            # chosen_list = [nums[a], nums[b], nums[b]]
            # if print_debug: print("chose: {} with sum {}".format(chosen_list, sum1))
            known_closest_sum = self.getCloserSum(sum1, known_closest_sum, target)

            # if the nums are all the same then we don't need to evaluate all the duplicates
            if nums[c1] == nums[b] and nums[b] == nums[c2]:
                left_bound = b
                right_bound = b

            # don't update left and right bounds since it's not clear where to go...
            left_sum = self.threeSumClosestHelper(a, c1, left_bound, right_bound, nums, target, known_closest_sum)
            right_sum = self.threeSumClosestHelper(a, c2, left_bound, right_bound, nums, target, known_closest_sum)

            known_closest_sum = self.getCloserSum(left_sum, known_closest_sum, target)
            known_closest_sum = self.getCloserSum(right_sum, known_closest_sum, target)

            print("known_closest_sum: {}".format(known_closest_sum))

            return known_closest_sum

        elif dist1 == sys.maxsize and dist2 != sys.maxsize:
            if print_debug: print("no dist1, but dist2")
            chosen_list = [nums[a], nums[b], nums[c2]]
            if print_debug: print("chose: {} with sum {}".format(chosen_list, sum2))
            known_closest_sum = self.getCloserSum(sum2, known_closest_sum, target)
            return self.threeSumClosestHelper(a, c2, left_bound, b, nums, target, known_closest_sum)

        elif dist1 != sys.maxsize and dist2 == sys.maxsize:
            if print_debug: print("no dist2, but dist1")
            chosen_list = [nums[a], nums[b], nums[c1]]
            if print_debug: print("chose: {} with sum {}".format(chosen_list, sum1))
            known_closest_sum = self.getCloserSum(sum1, known_closest_sum, target)
            return self.threeSumClosestHelper(a, c1, b, right_bound, nums, target, known_closest_sum)

        else:
            if dist1 < dist2:
                if print_debug: print("chose dist1")
                chosen_list = [nums[a], nums[b], nums[c1]]
                if print_debug: print("chose: {} with sum {}".format(chosen_list, sum1))
                known_closest_sum = self.getCloserSum(sum1, known_closest_sum, target)
                return self.threeSumClosestHelper(a, c1, left_bound, b, nums, target, known_closest_sum)

            else:
                if print_debug: print("chose dist2")
                chosen_list = [nums[a], nums[b], nums[c2]]
                if print_debug: print("chose: {} with sum {}".format(chosen_list, sum2))
                known_closest_sum = self.getCloserSum(sum2, known_closest_sum, target)
                return self.threeSumClosestHelper(a, c2, b, right_bound, nums, target, known_closest_sum)

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sorting will help us speed up when it comes to looking over duplicate elements
        nums.sort()

        known_closest_sum = sys.maxsize
        for a in range(0, len(nums) - 2):

            # skip over a's we've already seen
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            b = int((a + len(nums)) / 2)

            # put helper here
            sum_to_compare = self.threeSumClosestHelper(a, b, a, len(nums), nums, target, known_closest_sum)
            known_closest_sum = self.getCloserSum(sum_to_compare, known_closest_sum, target)

        return known_closest_sum

        #     leftBound = a
        #     rightBound = len(nums)
        #
        #     #compute b
        #     b = int((a + len(nums)) / 2)
        #
        #     while b != leftBound and b != rightBound:
        #         # compute c1
        #         c1 = int((leftBound + b) / 2)
        #         # compute c2
        #         c2 = int((b + rightBound) / 2)
        #
        #         dist1 = sys.maxsize
        #         dist2 = sys.maxsize
        #
        #         if c1 <= leftBound or c1 == b:
        #             pass
        #         else:
        #             sum1 = nums[a] + nums[b] + nums[c1]
        #             if print_debug: print("a:{} b:{} c1:{}".format(a, b, c1))
        #             if print_debug: print([nums[a], nums[b], nums[c1]])
        #             if print_debug: print("sum1 = {}".format(sum1))
        #             dist1 = abs(sum1 - target)
        #             if print_debug: print("dist1 = {}".format(dist1))
        #
        #         if c2 >= rightBound or c2 == b:
        #             pass
        #         else:
        #             sum2 = nums[a] + nums[b] + nums[c2]
        #             if print_debug: print("a:{} b:{} c2:{}".format(a, b, c2))
        #             if print_debug: print([nums[a], nums[b], nums[c2]])
        #             if print_debug: print("sum2 = {}".format(sum2))
        #             dist2 = abs(sum2 - target)
        #             if print_debug: print("dist2 = {}".format(dist2))
        #
        #         '''
        #         6 possible cases
        #         1. No distances available
        #         2. Distances are equal
        #         3. Dist1 is unavailable, Dist2 is available
        #         4. Dist1 is available, Dist2 is unavailable
        #         5. Dist1 < Dist2
        #         6. Dist1 > Dist2
        #         '''
        #         if dist1 == sys.maxsize and dist2 == sys.maxsize:
        #             if print_debug: print("no dist1 and no dist2, moving a forward")
        #             leftBound = b
        #             rightBound = b
        #         elif dist1 == dist2:
        #             if print_debug: print('dist1 equals dist2, only check one instance')
        #             # if distances are the same then c1 == b == c2
        #             chosenList = [nums[a], nums[b], nums[b]]
        #             if print_debug: print("chose: {} with sum {}".format(chosenList, sum1))
        #
        #             known_closest_sum = self.getCloserSum(sum1, known_closest_sum, target)
        #
        #             leftBound = b
        #             rightBound = b
        #         elif dist1 == sys.maxsize and dist2 != sys.maxsize:
        #             if print_debug: print("no dist1, but dist2")
        #             chosenList = [nums[a], nums[b], nums[c2]]
        #             if print_debug: print("chose: {} with sum {}".format(chosenList, sum2))
        #
        #             known_closest_sum = self.getCloserSum(sum2, known_closest_sum, target)
        #
        #             rightBound = b
        #             b = c2
        #         elif dist1 != sys.maxsize and dist2 == sys.maxsize:
        #             if print_debug: print("no dist2, but dist1")
        #             chosenList = [nums[a], nums[b], nums[c1]]
        #             if print_debug: print("chose: {} with sum {}".format(chosenList, sum1))
        #
        #             known_closest_sum = self.getCloserSum(sum1, known_closest_sum, target)
        #
        #             leftBound = b
        #             b = c1
        #         else:
        #             if dist1 < dist2:
        #                 if print_debug: print("chose dist1")
        #                 chosenList = [nums[a], nums[b], nums[c1]]
        #                 if print_debug: print("chose: {} with sum {}".format(chosenList, sum1))
        #
        #                 known_closest_sum = self.getCloserSum(sum1, known_closest_sum, target)
        #
        #                 rightBound = b
        #                 b = c1
        #             else:
        #                 if print_debug: print("chose dist2")
        #                 chosenList = [nums[a], nums[b], nums[c2]]
        #                 if print_debug: print("chose: {} with sum {}".format(chosenList, sum2))
        #
        #                 known_closest_sum = self.getCloserSum(sum2, known_closest_sum, target)
        #
        #                 leftBound = b
        #                 b = c2
        #
        #         if print_debug: print("------------------------")
        #
        # return known_closest_sum

if __name__ == "__main__":
    # result = Solution().threeSumClosest([-2, -1, 0, 1, 3, 3, 5], 9)
    # if print_debug: print(result)
    # if print_debug: print()
    # assert(result == 9)
    #
    # result = Solution().threeSumClosest([-2, -1, 0, 1, 3, 3, 5], -3)
    # if print_debug: print(result)
    # if print_debug: print()
    # assert(result == -3)
    #
    # result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
    # if print_debug: print(result)
    # if print_debug: print()
    # assert(result == 2)
    #
    # result = Solution().threeSumClosest(
    #     [89, -17, -41, 9, 56, -8, 40, 38, 98, -31, 80, -1, -40, -73, 28, 55, 15, 89, -83, 87, -42, -22, 61, 64, -94,
    #      -33, -38, 25, -20, -80, 37, 99, -72, 74, 16, -25, -21, -73, -73, -72, 65, -4, -72, 46, 60, 7, -25, -14, -58,
    #      -50, 14, -99, 88, 50, 75, -59, 94, -74, 25, 23, -10, -47, -1, -30, 81, -66, 54, -64, -1, 68, -1, 47, 55, -59,
    #      5, 64, 45, 83, -3, -38, -59, 46, 33, 54, 55, 9, -13, 50, -43, -48, 57, 97, -55, -13, -25, -9, -20, 63, 30, 88,
    #      -4, 74, 19, -87, -32],
    #     -297)
    # if print_debug: print(result)
    # if print_debug: print()
    # assert(result == -280)
    #
    # result = Solution().threeSumClosest(
    #     [-17, -12, -28, 77, -28, -63, -88, 40, 70, -97, -57, 15, 45, 37, -85, -74, 29, -80, 92, -62, 44, 26, -46, 54,
    #      74,
    #      11, 16, -64, -58, 56, 23, -77, 48, 7, -44, 92, -25, 85, -16, -87, 22, 52, 57, 66, 83, -90, 84, -56, -54, -2,
    #      -98,
    #      -52, 78, 93, 7, 49, -10, -34, 49, -14, 87, -69, 1, -67, 53, -85, 29, -4, -39, 66, 8, 42, -48, -18, -41, 94, -1,
    #      64,
    #      52, 90, 32, 53, -10, 0, -86, -94, -13, 45, 43, -23, 61, -78, -44, -30, -3, 32, 94, 30, 74, 51, 63, -87, 46, 3,
    #      61,
    #      -39, 9, 50, -23, 82, -100, -95, -31, -62, 88, -98, 22, 93, -81, 57, -56, 96, 78, -51, 24, -59, -80, 82, 77, 48,
    #      88,
    #      -81, -61, 44, -1, -15, 62, -89, 21, -72, -4, -1, -84, 61, -59, -91, -87, 23, -9, -55, 34, 34, -13, 68, -95,
    #      -80,
    #      -36, -49, 97, 80, -50, -35, -6, -16, 91, 59, 74, 53, -48, -55, -25, -74, 81, -47, -98, -66, -62, -83, 24, -16,
    #      -35,
    #      38],
    #     -132)
    # if print_debug: print(result)
    # if print_debug: print()
    # assert(result == -132)
    #
    # result = Solution().threeSumClosest([-2, 3, 3, 3, 3, 3, 5], 9)
    # if print_debug: print(result)
    # if print_debug: print()
    # assert(result == 9)
    #
    # result = Solution().threeSumClosest([1,2,5,10,11], 12)
    # if print_debug: print(result)
    # if print_debug: print()
    # assert (result == 13)

    result = Solution().threeSumClosest([-20, -19, -19, -19, -19, -19, -19, -18, -18, -17, -17, -17, -16, -16, -16, -15, -15, -14, -14, -14, -13, -13, -13, -12, -12, -12, -11, -10, -10, -10, -9, -9, -9, -9, -7, -7, -7, -6, -5, -5, -5, -4, -4, -3, -3, -3, -2, -2, -2, -2, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8, 9, 9, 10, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 20, 20, 20],
                                         -59)
    if print_debug: print(result)
    if print_debug: print()
    assert(result == -58)

    result = Solution().threeSumClosest([1, 6, 9, 14, 16, 70], 81)
    if print_debug: print(result)
    if print_debug: print()
    assert(result == 80)
