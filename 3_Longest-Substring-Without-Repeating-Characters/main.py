# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke",
# with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution_1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest_substring_found = ""
        substring = ""
        start_idx = 0

        i = 0
        while i < len(s):
            if (s[i] not in substring):
                substring += s[i]
                #replace size if longer
                if (len(substring) > len(longest_substring_found)):
                    longest_substring_found = substring
            else:
                #update substring starting location to one after where we started
                start_idx += 1
                i = start_idx
                substring = s[i]

            #increment loop
            i += 1

        print(longest_substring_found)
        return len(longest_substring_found)

class Solution_2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest_substring_found = ""
        substring = ""
        start_idx = 0
        used_chars = set([]) #will be used to speed up checking against used chars

        i = 0
        while i < len(s):
            if (s[i] not in used_chars):
                substring += s[i]
                #add to set
                used_chars.add(s[i])
                # replace size if longer
                if (len(substring) > len(longest_substring_found)):
                    longest_substring_found = substring
            else:
                # update substring starting location to one after where we started
                start_idx += 1
                i = start_idx
                substring = s[i]

                #clear the set and add again
                used_chars.clear()
                used_chars.add(s[i])

            # increment loop
            i += 1

        print(longest_substring_found)
        return len(longest_substring_found)

if __name__ == "__main__":

    """
    Solution 1
    runtime complexity: O(n^3)
      iterate through all the characters in s
      elements will be visited a total of:
      1 + 2 + 3 + ... + (n - 1) + n  total times
      this is a known series of n(n-1)/2
      the loop visiting everything is O(n^2)
      'not in' runs in linear time for each iteration since it needs to check against all elements - O(n)

      worst case scenario

    space complexity: O(n)
      constantly need to keep track of the existing longest substring
    """

    print("Solution 1 ===============")
    assert(Solution_1().lengthOfLongestSubstring("abcabcbb") == 3)
    assert(Solution_1().lengthOfLongestSubstring("bbbbb") == 1)
    assert(Solution_1().lengthOfLongestSubstring("pwwkew") == 3)
    assert(Solution_1().lengthOfLongestSubstring("dvdf") == 3)
    """
    Solution 2
    runtime complexity: O(nm)
      iterate through all the characters in s
      elements will be visited a total of:
      1 + 2 + 3 + ... + (n - 1) + n  total times
      this is a known series of n(n-1)/2
      the loop visiting everything is O(n^2)
      'not in' runs in constant time for each iteration

    space complexity: O(2n) -> O(n)
      constantly need to keep track of the existing longest substring and the set
    """
    print("Solution 2 ===============")
    assert(Solution_2().lengthOfLongestSubstring("abcabcbb") == 3)
    assert(Solution_2().lengthOfLongestSubstring("bbbbb") == 1)
    assert(Solution_2().lengthOfLongestSubstring("pwwkew") == 3)
    assert(Solution_2().lengthOfLongestSubstring("dvdf") == 3)

    """
    Solution 3
    You can cache the work done by the creation of the substring.
    i.e. ABCABCBB
    A
    AB
    ABC
    ABCA - Duplicate
    B
    BC  
    BCA - all this work could have been cached
    
    Instead of staring over from B, keep a window of valid elements
    """