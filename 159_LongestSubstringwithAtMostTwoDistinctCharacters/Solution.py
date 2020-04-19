class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest_substring = ''
        char_range_set = dict()
        current = 0

        # go through every character
        while current < len(s):
            curr_char = s[current]
            if curr_char not in char_range_set:
                # first time this character is seen, add its starting/ending position
                char_range_set[curr_char] = [current, current]

                # check if we have a longer substring
                (start, end) = self.getSubstringRange(char_range_set)
                if len(longest_substring) < len(s[start: end + 1]):
                    longest_substring = s[start: end + 1]

                if len(char_range_set.keys()) > 2:
                    first_key = list(char_range_set.keys())[0]
                    # update starting position
                    current = self.getStartingPos(char_range_set)
                    # reset all the ranges
                    char_range_set.clear()
                else:
                    # move forward 1 char
                    current += 1
            else:
                #update ending value in charRangeSet
                char_range_set[curr_char][1] = current
                # move forward 1 char
                current += 1

        # after loop finishes we need to process the last char
        (start, end) = self.getSubstringRange(char_range_set)
        if len(longest_substring) < len(s[start: end + 1]):
            longest_substring = s[start: end + 1]

        print(longest_substring)
        return len(longest_substring)

    def getStartingPos(self, range_set):
        '''
        Given a range set, return the index of the last
        :param range_set:
        :return:
        '''
        keys = list(range_set.keys())
        first_char = keys[0]
        second_char = keys[1]
        if range_set[first_char][1] < range_set[second_char][0]:
            # no overlap
            return range_set[second_char][0]
        elif range_set[second_char][1] < range_set[first_char][0]:
            # no overlap
            return range_set[first_char][0]
        else:
            # overlap
            return max(range_set[first_char][1], range_set[second_char][1])

    def getSubstringRange(self, range_set):
        if len(range_set.keys()) == 0:
            # if there are no chars then range is 0
            return 0, 0
        elif len(range_set.keys()) < 2:
            # if there is 1 char then range is just that char
            keys = list(range_set.keys())
            key = keys[0]
            # starting and ending position
            return range_set[key][0], range_set[key][1]
        else:
            # if there are 2 chars then range is combination of those chars
            keys = list(range_set.keys())
            first_char = keys[0]
            second_char = keys[1]
            starting_idx = min(range_set[first_char][0], range_set[second_char][0])
            ending_idx = max(range_set[first_char][1], range_set[second_char][1])
            return starting_idx, ending_idx

if __name__ == "__main__":

    sol = Solution()

    range_set = {'a': [0, 5], 'b': [6, 10]}
    start, end = sol.getSubstringRange(range_set)
    assert start == 0
    assert end == 10

    range_set = {'a': [0, 6], 'b': [5, 10]}
    start, end = sol.getSubstringRange(range_set)
    assert start == 0
    assert end == 10

    range_set = {'b': [6, 10]}
    start, end = sol.getSubstringRange(range_set)
    assert start == 6
    assert end == 10

    range_set = {'a': [0, 5], 'b': [6, 10]}
    starting_pos = sol.getStartingPos(range_set)
    assert starting_pos == 6

    range_set = {'a': [0, 7], 'b': [6, 10]}
    starting_pos = sol.getStartingPos(range_set)
    assert starting_pos == 10

    range_set = {'a': [0, 10], 'b': [1, 9]}
    starting_pos = sol.getStartingPos(range_set)
    assert starting_pos == 10

    range_set = {'a': [0, 6], 'b': [5, 11]}
    starting_pos = sol.getStartingPos(range_set)
    print(starting_pos)

    result = sol.lengthOfLongestSubstringTwoDistinct('eceba')
    assert result == 3

    result = sol.lengthOfLongestSubstringTwoDistinct('ccaabbb')
    assert result == 5

    result = sol.lengthOfLongestSubstringTwoDistinct('abc')
    assert result == 2

    result = sol.lengthOfLongestSubstringTwoDistinct('a')
    assert result == 1

    result = sol.lengthOfLongestSubstringTwoDistinct('')
    assert result == 0

    result = sol.lengthOfLongestSubstringTwoDistinct('cacacabbbbccc')
    assert result == 7

    result = sol.lengthOfLongestSubstringTwoDistinct('abcdeegfg')
    assert result == 3




