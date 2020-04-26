from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = self.charFreq(t)
        s_freq = self.charFreq(s)

        # check to make sure t_freq is even possible
        for key, value in t_freq.items():
            if s_freq[key] < value:
                return ""

        position_map = {}

        min_distance = None

        # if we've reached this point it's possible, now scan
        for i in range(len(s)):
            # determine if s[i] is needed
            if s[i] not in t_freq:
                continue

            # update position map
            position_map[s[i]] = i

            # check if we have all characters needed to compare
            if not self.containsAllKeys(position_map, t_freq):
                continue

            # if we've reached this point we have all our chars, compute distance
            min_idx, max_idx = self.computePosMinMax(position_map)

            # + 1 to count last char
            distance = max_idx - min_idx + 1
            if min_distance is None:
                min_distance = (min_idx, max_idx + 1, distance)
            elif distance < min_distance[2]:
                min_distance = (min_idx, max_idx + 1, distance)

        substring = s[min_distance[0]:min_distance[1]]
        return substring

    def containsAllKeys(self, position_map, t_freq):
        contains_all_keys = True
        for key in t_freq.keys():
            if key not in position_map:
                contains_all_keys = False
        return contains_all_keys

    def charFreq(self, string):
        freq = defaultdict(int)
        for s in string:
            freq[s] += 1
        return freq

    def computePosMinMax(self, position_map):
        min_idx = float('inf')
        max_idx = float('-inf')
        for key, value in position_map.items():
            min_idx = min(min_idx, value)
            max_idx = max(max_idx, value)
        return min_idx, max_idx


if __name__ == "__main__":
    sol = Solution()

    output = sol.minWindow('ADOBECODEBANC', 'ABC')
    assert output == 'BANC'

    output = sol.minWindow('A', 'ABC')
    assert output == ''

    output = sol.minWindow('A', 'A')
    assert output == 'A'

    output = sol.minWindow('ADOBECODEBANC', 'ABE')
    assert output == 'EBA'

    """
    This does not work for duplicates
    """
