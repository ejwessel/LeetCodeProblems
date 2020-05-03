from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        missing_ranges = []

        # handle when list is empty
        if not nums:
            missing_ranges.append([lower, upper])
            return self.format_output(missing_ranges)

        # handle if lower bound is not in nums
        if lower != nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        # handle nums ranges
        for i in range(len(nums) - 1):
            # if the numbers are the same then there is no range in between
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] + 1 != nums[i + 1]:
                missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])

        # handle if upper bound is not in nums
        if upper != nums[-1]:
            missing_ranges.append([nums[-1] + 1, upper])

        return self.format_output(missing_ranges)

    def format_output(self, missing_ranges):
        output = []
        for num_range in missing_ranges:
            if num_range[0] == num_range[1]:
                output.append(f'{num_range[0]}')
            else:
                output.append(f'{num_range[0]}->{num_range[1]}')
        return output



if __name__ == '__main__':
    sol = Solution()

    result = sol.findMissingRanges([1, 1, 1], 1, 1)
    assert result == []

    result = sol.findMissingRanges([], 1, 1)
    assert result == ['1']

    result = sol.findMissingRanges([], 1, 99)
    assert result == ['1->99']

    result = sol.findMissingRanges([], -10, 99)
    assert result == ['-10->99']

    result = sol.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
    assert result == ['2', '4->49', '51->74', '76->99']

    result = sol.findMissingRanges([2, 4, 8], 0, 99)
    assert result == ['0->1', '3', '5->7', '9->99']

    result = sol.findMissingRanges([2, 4, 8], -1, 99)
    assert result == ['-1->1', '3', '5->7', '9->99']

    result = sol.findMissingRanges([2, 4, 99], -5, 99)
    assert result == ['-5->1', '3', '5->98']

    result = sol.findMissingRanges([2, 99], -5, 99)
    assert result == ['-5->1', '3->98']
