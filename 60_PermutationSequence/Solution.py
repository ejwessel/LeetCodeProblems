from math import factorial
from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        list = []
        for i in range(n):
            list.append(i + 1)

        result = self.recursiveFind(list, k, 0)
        result = ''.join(result)
        return result

    def recursiveFind(self, list, k, lower_rng):
        if len(list) == 1:
            return [str(list[0])]

        # find the range closest to our target that doesn't go over
        selected_idx = 0
        lower_range = selected_idx
        for j in range(len(list)):
            # -1 for remaining items in list that will be used
            upper_range = lower_rng + (j + 1) * factorial(len(list) - 1)
            selected_idx = j
            if upper_range >= k:
                break
            lower_range = upper_range

        list_without_selected = list[:selected_idx] + list[selected_idx + 1:]
        result = [str(list[selected_idx])] + self.recursiveFind(list_without_selected, k, lower_range)
        return result



if __name__ == "__main__":
    sol = Solution()

    '''
    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.
    '''

    # p = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # count = 1
    # for i in p:
    #     if count == 360000:
    #         print(i)
    #     count += 1

    result = sol.getPermutation(1, 1)
    assert result == '1'

    result = sol.getPermutation(4, 9)
    assert result == '2314'

    result = sol.getPermutation(3, 3)
    assert result == '213'

    result = sol.getPermutation(4, 22)
    assert result == '4231'

    result = sol.getPermutation(4, 1)
    assert result == '1234'

    result = sol.getPermutation(9, 360000)
    assert result == '983765421'


