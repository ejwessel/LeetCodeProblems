# not all integers are distinct, return all possible permutations
# remember total number of answers is n!
from typing import List

class Solution:
    def __init__(self):
        self.solutions = []
        self.seen_sets = set()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self._permute(nums, [])
        return self.solutions

    def _permute(self, input_values, current_permutation):
        if len(input_values) == 0 and tuple(current_permutation) not in self.seen_sets:
            self.solutions.append(current_permutation)
            self.seen_sets.add(tuple(current_permutation))
        else:
            for i in range(len(input_values)):
                # skip over i and formulate a new list with the element missing
                new_input = input_values[:i] + input_values[i + 1:]
                self._permute(new_input, current_permutation + [input_values[i]])


if __name__ == "__main__":
    sol = Solution()
    input = [1, 2, 3]
    result = sol.permuteUnique(input)
    assert result == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    sol = Solution()
    input = [1, 1, 2]
    result = sol.permuteUnique(input)
    assert result == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
