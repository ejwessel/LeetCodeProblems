# all integers are distinct, return all possible permutations
# remember total number of answers is n!
from typing import List
from itertools import permutations

class Solution:
    def __init__(self):
        self.solutions = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self._permute(nums, [], set())
        return self.solutions

    def _permute(self, input_values, current_permutation, used_set):
        if len(input_values) == len(current_permutation):
            self.solutions.append(current_permutation)
        else:
            for element in input_values:
                # skip over used elements
                if element in used_set:
                    continue
                new_set = used_set.copy()
                new_set.add(element)
                self._permute(input_values, current_permutation + [element], new_set)


if __name__ == "__main__":
    sol = Solution()
    input = [1, 2, 3]
    result = sol.permute(input)
    assert result == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
