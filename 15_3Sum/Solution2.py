class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answersList = []
        twoSumDict = {}
        for a in range(0, len(nums) - 2):
            for b in range(a + 1, len(nums) - 1):

                a_b_sum = nums[a] + nums[b]
                a_b_two_new_list = [nums[a], nums[b]]
                a_b_two_new_list.sort()

                # make empty entry if the key doesn't exist
                if a_b_sum not in twoSumDict:
                    twoSumDict[a_b_sum] = []

                # add the list if it's not wihin our lists already
                if a_b_two_new_list not in twoSumDict[a_b_sum]:
                    print("adding {} to cache under {}".format(a_b_two_new_list, a_b_sum))
                    twoSumDict[a_b_sum].append(a_b_two_new_list)
                    print("CACHE: {}".format(twoSumDict))

                for c in range(b + 1, len(nums)):
                    # check against twoSumDict if we've already seen a two sum before
                    # print("EVALUATING : {} {} {}".format(nums[a], nums[b], nums[c]))

                    num = nums[c]
                    num_comp = -nums[c] #num_complement

                    # print("looking for opposite of {} : {}".format(num, num_comp))
                    if num_comp in twoSumDict:
                        # print("complement has been found")
                        # go through all the lists for that value and make answer lists
                        for list in twoSumDict[num_comp]:
                            newList = list.copy()
                            newList.append(num)
                            newList.sort()

                            if newList not in answersList:
                                answersList.append(newList)
                                print("Complement of {} : {} found".format(num, num_comp))
                                print("EVALUATING : {} {} {}".format(nums[a], nums[b], nums[c]))
                                print("Adding {} to answers".format(newList))
                                print("ANSWERS LIST {}".format(answersList))
                    else:
                        print("complement not found")
                        pass

        return answersList

if __name__ == "__main__":

    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print(result)

    result = Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
    # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
    print(result)