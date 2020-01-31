class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sorting will help us speed up when it comes to looking over duplicate elements
        nums.sort()
        print(nums)

        closestList = None
        closestSum = None
        for a in range(0, len(nums) - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums) - 1):
                if b > (a + 1) and nums[b] == nums[b - 1]:
                    continue
                for c in range(b + 1, len(nums)):
                    if c > (b + 1) and nums[c] == nums[c - 1]:
                        continue

                    sum = nums[a] + nums[b] + nums[c]
                    if closestSum is None:
                        closestSum = sum
                        closetList = [nums[a], nums[b], nums[c]]
                    else:
                        sum_dist = abs(sum - target)
                        closest_sum_dist = abs(closestSum - target)
                        if sum_dist < closest_sum_dist:
                            closestSum = sum
                            closetList = [nums[a], nums[b], nums[c]]

        return closestSum, closetList

if __name__ == "__main__":
    result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print(result)
    print()
    assert(result[0] == 2)

    result = Solution().threeSumClosest([89,-17,-41,9,56,-8,40,38,98,-31,80,-1,-40,-73,28,55,15,89,-83,87,-42,-22,61,64,-94,-33,-38,25,-20,-80,37,99,-72,74,16,-25,-21,-73,-73,-72,65,-4,-72,46,60,7,-25,-14,-58,-50,14,-99,88,50,75,-59,94,-74,25,23,-10,-47,-1,-30,81,-66,54,-64,-1,68,-1,47,55,-59,5,64,45,83,-3,-38,-59,46,33,54,55,9,-13,50,-43,-48,57,97,-55,-13,-25,-9,-20,63,30,88,-4,74,19,-87,-32],
                                        -297)
    print(result)
    print()
    assert(result[0] == -280)

    result = Solution().threeSumClosest([-17, -12, -28, 77, -28, -63, -88, 40, 70, -97, -57, 15, 45, 37, -85, -74, 29, -80, 92, -62, 44, 26, -46, 54, 74,
     11, 16, -64, -58, 56, 23, -77, 48, 7, -44, 92, -25, 85, -16, -87, 22, 52, 57, 66, 83, -90, 84, -56, -54, -2, -98,
     -52, 78, 93, 7, 49, -10, -34, 49, -14, 87, -69, 1, -67, 53, -85, 29, -4, -39, 66, 8, 42, -48, -18, -41, 94, -1, 64,
     52, 90, 32, 53, -10, 0, -86, -94, -13, 45, 43, -23, 61, -78, -44, -30, -3, 32, 94, 30, 74, 51, 63, -87, 46, 3, 61,
     -39, 9, 50, -23, 82, -100, -95, -31, -62, 88, -98, 22, 93, -81, 57, -56, 96, 78, -51, 24, -59, -80, 82, 77, 48, 88,
     -81, -61, 44, -1, -15, 62, -89, 21, -72, -4, -1, -84, 61, -59, -91, -87, 23, -9, -55, 34, 34, -13, 68, -95, -80,
     -36, -49, 97, 80, -50, -35, -6, -16, 91, 59, 74, 53, -48, -55, -25, -74, 81, -47, -98, -66, -62, -83, 24, -16, -35,
     38],
    -132)
    print(result)
    print()
    assert(result[0] == -132)

    result = Solution().threeSumClosest([-2, -1, 1, 0, 3, 3, 5], -3)
    print(result)
    print()

    result = Solution().threeSumClosest([-2, -1, 1, 0, 3, 3, 5], 9)
    print(result)
    print()

    result = Solution().threeSumClosest([-2, 3, 3, 3, 3, 3, 5], 9)
    print(result)
    print()

    result = Solution().threeSumClosest([1,2,5,10,11], 12)
    print(result)
    print()

    result = Solution().threeSumClosest([-20, -19, -19, -19, -19, -19, -19, -18, -18, -17, -17, -17, -16, -16, -16, -15, -15, -14, -14, -14, -13, -13, -13, -12, -12, -12, -11, -10, -10, -10, -9, -9, -9, -9, -7, -7, -7, -6, -5, -5, -5, -4, -4, -3, -3, -3, -2, -2, -2, -2, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8, 9, 9, 10, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 20, 20, 20],
                                         -59)
    print(result)
    print()
