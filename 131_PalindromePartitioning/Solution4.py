from collections import defaultdict

class Solution:
    def __init__(self):
        self.palindrome = {}
        self.memo = defaultdict(list) # will contain lists of all the possible partitions

    def partition(self, s: str):
        self._partition(s)
        return self.memo[s]

    def _partition(self, s: str):
        # start at 1 and go 1 past the end because otherwise '' is looked at on the left side and it's a wasted cycle
        for i in range(1, len(s) + 1):
            left_sub = s[:i]
            right_sub = s[i:]

            # if the left is not a palindrome, there is no work
            is_palindrome = (left_sub in self.palindrome and self.palindrome[left_sub]) or (left_sub == left_sub[::-1])
            if not is_palindrome:
                self.palindrome[left_sub] = False
                continue

            self.palindrome[left_sub] = True

            # if the right is the end of the string
            if right_sub is '':
                self.memo[left_sub].append([left_sub])
                continue

            # if the right sub is not computed, then attempt to compute it
            if right_sub not in self.memo:
                self._partition(right_sub)

            # right sub still may not have a solution and therefore we can ignore it
            if right_sub in self.memo:
                partitions = self.memo[right_sub]
                for partition in partitions:
                    temp_list = [left_sub]
                    for elements in partition:
                        temp_list.append(elements)
                    self.memo[s].append(temp_list)

if __name__ == "__main__":

    sol = Solution()
    result = sol.partition("aab")
    assert result == [['a', 'a', 'b'], ['aa', 'b']]

    sol = Solution()
    result = sol.partition("abbac")
    assert result == [['a', 'b', 'b', 'a', 'c'], ['a', 'bb', 'a', 'c'], ['abba', 'c']]

    sol = Solution()
    result = sol.partition("a")
    assert result == [['a']]

    sol = Solution()
    result = sol.partition("")
    assert result == []
