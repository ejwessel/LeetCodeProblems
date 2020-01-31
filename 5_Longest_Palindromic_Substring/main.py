
class Solution_1:
    def __init__(self):
        self.string_cache = set([])
        self.longest_string = ""

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Use a Window √
        Have a set to skip over strings we've already seen √
        Start with the entire size of the string and check if it's a palindrome
        
        Once we've found a palindrome return that palindrome
        Otherwise reduce the window by 1
        Split the window into [b, e - 1] and [b + 1, e] where b and e are beginning and end
        
        optimizations come from use of set and not checking things that are smaller than longest
        """
        # print("longest: " + self.longest_string)
        # print(s)

        #only continue if we haven't seen this string combination yet
        if s in self.string_cache:
            return ""

        #regardless of finding a palindrome or not cache any string and it's opposite
        self.string_cache.add(s)
        self.string_cache.add(s[::-1])

        #String too short, we can't process, return empty string
        if len(s) <= 0:
            return ""

        #no reason to continue recursive stack if all resulting depth strings are smaller
        if (len(s) <= len(self.longest_string)):
            return ""

        if is_palindrome(s):
            # print("%s is palindrome" % s)
            return s
        else:
            #shorten window by 1 left
            left_s = s[:len(s) - 1]
            # print("left_s: " + left_s)
            left_result = self.longestPalindrome(left_s)

            #shorten window by 1 right
            right_s = s[1:len(s)]
            # print("right_s: " + right_s)
            right_result = self.longestPalindrome(right_s)

            #after coming back from our recursive step we may have found a better suited candidate
            #get the larger of the two strings
            temp = None
            if len(left_result) >= len(right_result):
                temp = left_result
            else:
                temp = right_result

            #compare candidate to longest and overwrite if better
            if len(temp) > len(self.longest_string):
                self.longest_string = temp

            return self.longest_string


class Solution_2:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        #handle invalid strings
        if s is None or s is "":
            return ""

        longest_palindrome = ""
        #iterate over all the middles computing the longest palindrome
        for i in range(0, len(s)):
            #handle even and off middles

            odd_string = self.get_palindrome_around_center(s, i, i)
            # print("even pal: " + even_pali)
            even_string = self.get_palindrome_around_center(s, i, i + 1)
            # print("odd pal: "+ odd_pali)

            #determine which one is longer and overwrite
            temp = ""
            if len(odd_string) > len(even_string):
                temp = odd_string
            else:
                temp = even_string

            if len(temp) > len(longest_palindrome):
                longest_palindrome = temp

        return longest_palindrome

    def get_palindrome_around_center(self, s, start, end):
        """
        expands a string around some center and returns the length of that string
        :param s: the string we're going to analyze
        :param start: starting location within that string
        :param end: starting end location (inclusive at that index) within that string
        :return: string the palindromic string
        """

        #stop loop if the bounds are never exited
        while(start >= 0 and end < len(s)):
            # print("start: " + str(start) + " end: " + str(end))

            #if the start and ends don't match then don't update the positions
            if s[start] != s[end]:
                break

            # only update the positions if start and end are the same
            start -= 1
            end += 1

        #if the while loop stopped then we need to account for the start and end offsets
        # start needs to increase by 1
        # end needs to decrease by 1
        # note: substring is exclusive of end
        return s[start + 1: end]


def is_palindrome(s):
    """
    Goes halfway through the list and checks to see if it's a palindrome
    :param s:
    :return: boolean true/false
    """

    #palindrome must have a size 1 or more
    if len(s) < 1:
        return False

    last_indx = len(s) - 1
    #palindrome is the same front the back, we only need to visit halfway
    for i in range(0, int(len(s) / 2)):
        if s[i] == s[last_indx - i]:
            continue
        else:
            return False
    return True

def is_palindrome_simple(s):
    if len(s) < 1:
        return False

    return s == s[::-1]

if __name__ == "__main__":

    #Solution 1
    # Test is_palindrome()
    assert(is_palindrome("abba") == True)
    assert(is_palindrome("aba") == True)
    assert(is_palindrome("ab") == False)
    assert(is_palindrome("abb") == False)
    assert(is_palindrome("a") == True)
    assert(is_palindrome("") == False)

    # Test is_palindrome_simple()
    assert(is_palindrome_simple("abba") == True)
    assert(is_palindrome_simple("aba") == True)
    assert(is_palindrome_simple("ab") == False)
    assert(is_palindrome_simple("abb") == False)
    assert(is_palindrome_simple("a") == True)
    assert(is_palindrome_simple("") == False)

    sol = Solution_1()
    assert(sol.longestPalindrome("babad") == "bab")
    sol = Solution_1()
    assert(sol.longestPalindrome("cbbd") == "bb")

    sol = Solution_1()
    assert(sol.longestPalindrome("babaddtattarrattatddetartrateedredividerb") == "ddtattarrattatdd")
    sol = Solution_1()
    assert(sol.longestPalindrome("cwziydanrqvsdtvnnqgjnbrvvwxwqojeqgxhwxdoktjktulemwpbeqscbbtbfvkxsrjetfdrovcrdwzfmnnihtgxybuairswfewvpuscocqifuwylhssldpjrawqdrbvkykpaggspbfrulcktpbofchzikhzxhpocgvdbwpewpywsgqbczmamprklaoovcfecwchhmsaqkhvuvvzjblmgvqpqtnlipgqsanvovylpmxlmxvymppdykphhaamtxjnnlsqfwjwhyywgurteaummwhvavxbcpgrfffxrowluqmqjaugryxdmwvyokdcfcvcytxpixbvwrdgzctejdoaavgtezexmvxgrkpnayvfarkyoruofqmpnsqdzojxqrjsnfwsbzjmaoigytygukqlrcqaxazvmytgfghdczvzphfdbnxtklaiqqsotavdmhiaermluafheowcobjqmrkmlzyas") == "gytyg")
    sol = Solution_1()
    assert(sol.longestPalindrome("azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc") == "sooos")
    sol = Solution_1()
    assert(sol.longestPalindrome("lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc") == "lbabl")

    #Solution 2
    assert(Solution_2().get_palindrome_around_center("hello", 1, 1) == "e")
    assert(Solution_2().get_palindrome_around_center("abb", 1, 2) == "bb")
    assert(Solution_2().get_palindrome_around_center("abba", 1, 2) == "abba")
    assert(Solution_2().get_palindrome_around_center("a", 0, 0) == "a")
    assert(Solution_2().get_palindrome_around_center("a", 0, 1) == "")

    assert(Solution_2().longestPalindrome("babad") == "bab")
    assert(Solution_2().longestPalindrome("cbbd") == "bb")

    assert(Solution_2().longestPalindrome("babaddtattarrattatddetartrateedredividerb") == "ddtattarrattatdd")
    assert(Solution_2().longestPalindrome("cwziydanrqvsdtvnnqgjnbrvvwxwqojeqgxhwxdoktjktulemwpbeqscbbtbfvkxsrjetfdrovcrdwzfmnnihtgxybuairswfewvpuscocqifuwylhssldpjrawqdrbvkykpaggspbfrulcktpbofchzikhzxhpocgvdbwpewpywsgqbczmamprklaoovcfecwchhmsaqkhvuvvzjblmgvqpqtnlipgqsanvovylpmxlmxvymppdykphhaamtxjnnlsqfwjwhyywgurteaummwhvavxbcpgrfffxrowluqmqjaugryxdmwvyokdcfcvcytxpixbvwrdgzctejdoaavgtezexmvxgrkpnayvfarkyoruofqmpnsqdzojxqrjsnfwsbzjmaoigytygukqlrcqaxazvmytgfghdczvzphfdbnxtklaiqqsotavdmhiaermluafheowcobjqmrkmlzyas") == "gytyg")
    assert(Solution_2().longestPalindrome("azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc") == "sooos")
    assert(Solution_2().longestPalindrome("lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc") == "lbabl")
