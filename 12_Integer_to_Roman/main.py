import math

class Solution1:

    number_num_dict = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M"
    }

    MAX_NUMERAL_VAL = 1000

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        numeral_rep_list = []

        while(num > 0):
            # print(num)

            left_digit = self.getLeftDigit(num)
            num_zeros = self.getNumDigits(num) - 1

            # print("%d %d" % (left_digit, num_zeros))

            largest_denom = math.pow(10, num_zeros)
            lookup_val = int(left_digit * largest_denom)
            num -= lookup_val

            #handle if lookup value is greater than max val
            if lookup_val > self.MAX_NUMERAL_VAL:
                numeral_denom = []
                for i in range(0, left_digit):
                    numeral_lookup = self.number_num_dict[largest_denom]
                    # print(numeral_lookup)
                    numeral_denom.append(numeral_lookup)

                #consolidate appended numeral
                numeral = ''.join(numeral_denom)
                numeral_rep_list.append(numeral)
                # print(numeral)
            else:
                numeral_lookup = self.number_num_dict[lookup_val]
                numeral_rep_list.append(numeral_lookup)
                # print(numeral_lookup)

        #consolidate all collected numerals
        numeral_rep_string = ''.join(numeral_rep_list)
        return numeral_rep_string

    def getLeftDigit(self, num):
        num_string = str(num)
        return int(num_string[0])

    def getNumDigits(self, num):
        return len(str(num))

class Solution2:

    number_num_dict = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M"
    }

    MAX_NUMERAL_VAL = 1000

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        numeral_rep_list = []

        while(num > 0):
            # print(num)

            right_digit = self.getRightDigit(num)
            num_zeros = self.getNumTens(num)

            # print("%d %d" % (left_digit, num_zeros))

            smallest_denom = math.pow(10, num_zeros)
            lookup_val = int(right_digit * smallest_denom)

            # print(lookup_val)

            # update number so it doesn't have the smallest denomination anymore
            num -= lookup_val

            #handle if lookup value is greater than max val
            if lookup_val > self.MAX_NUMERAL_VAL:
                numeral_denom = []
                num_max_numeral = int(lookup_val / self.MAX_NUMERAL_VAL)
                for i in range(0, num_max_numeral):
                    numeral_lookup = self.number_num_dict[self.MAX_NUMERAL_VAL]
                    # print(numeral_lookup)
                    numeral_denom.append(numeral_lookup)

                #consolidate appended numeral
                numeral = ''.join(numeral_denom)
                numeral_rep_list.append(numeral)
                # print(numeral)
            else:
                numeral_lookup = self.number_num_dict[lookup_val]
                numeral_rep_list.append(numeral_lookup)
                # print(numeral_lookup)

        #consolidate all collected numerals
        numeral_rep_list.reverse()
        # print(numeral_rep_list)
        numeral_rep_string = ''.join(numeral_rep_list)
        return numeral_rep_string

    def getRightDigit(self, num):
        remainder = int(num % 10)
        num = num / 10
        while (remainder == 0):
            remainder = int(num % 10)
            num = num / 10
        return remainder

    def getNumTens(self, num):
        num_tens = 0
        remainder = num % 10
        num = num / 10
        while(remainder == 0):
            num_tens += 1
            remainder = num % 10
            num = num / 10
        return num_tens

class Solution3:
    number_num_dict = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M"
    }

    MAX_NUMERAL_VAL = 1000

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # this will hold the numeral representation for each ten's place
        # we'll be adding to this in reverse order since we'll be moving from LSD to MSD
        numeral_rep_list = []

        # keep track of what position we're at as we're building the roman numeral
        # we start at the 0th 10's position
        tens_place = 1

        # if a number is > 0 then there is a number to evaluate
        while (num > 0):
            # print(num)

            right_digit = self.getRightDigit(num)
            # print("Right digit we're evaluating at position %d : %d" % (tens_place, right_digit))
            lookup_val = int(right_digit * tens_place)
            # print("Value to look up %d" % lookup_val)

            # update number so it doesn't have the smallest denomination anymore
            num = int(num / 10)

            # account for dropping the least most significant digit
            tens_place *= 10

            # if the number we're evaluating is a 0,
            # we should just continue, there is no numeral for 0
            if lookup_val == 0:
                next

            # handle if lookup value is greater than max val
            elif lookup_val > self.MAX_NUMERAL_VAL:
                new_numeral_rep = []
                num_of_max_numerals = int(lookup_val / self.MAX_NUMERAL_VAL)

                # repeat max numerals and generate numeral representation
                for i in range(0, num_of_max_numerals):
                    numeral_lookup = self.number_num_dict[self.MAX_NUMERAL_VAL]
                    new_numeral_rep.append(numeral_lookup)

                # consolidate appended numeral and add to overall numeral list
                numeral = ''.join(new_numeral_rep)
                numeral_rep_list.append(numeral)
                # print(numeral)

            # Look up numeral value in our dictionary mapping
            else:
                numeral_lookup = self.number_num_dict[lookup_val]
                numeral_rep_list.append(numeral_lookup)
                # print(numeral_lookup)

        # Only after we have evaluated all 10's places and have their numeral representation,
        # we'll make the actual numeral

        # represent left to right instead of right to left
        numeral_rep_list.reverse()
        numeral_rep_string = ''.join(numeral_rep_list)
        return numeral_rep_string

    def getRightDigit(self, num):
        return int(num % 10)

if __name__ == "__main__":

    #Solution 1
    #test left most digit
    assert(Solution1().getLeftDigit(5431) == 5)
    assert(Solution1().getLeftDigit(5) == 5)

    #test num digits
    assert(Solution1().getNumDigits(5431) == 4)
    assert(Solution1().getNumDigits(5) == 1)
    assert(Solution1().getNumDigits(1000) == 4)

    # test intToRoman
    assert(Solution1().intToRoman(3) == "III")
    assert(Solution1().intToRoman(4) == "IV")
    assert(Solution1().intToRoman(9) == "IX")
    assert(Solution1().intToRoman(58) == "LVIII")
    assert(Solution1().intToRoman(1994) == "MCMXCIV")
    assert(Solution1().intToRoman(123) == "CXXIII")
    assert(Solution1().intToRoman(5431) == "MMMMMCDXXXI")
    assert(Solution1().intToRoman(1000) == "M")

    # Will fail on because it doesn't properly parse
    # assert (Solution2().intToRoman(10999) == "MMMMMMMMMMCMXCIX")
    # assert (Solution2().intToRoman(20999) == "MMMMMMMMMMMMMMMMMMMMCMXCIX")

    #Solution 2
    #test right most digit
    assert(Solution2().getRightDigit(5431) == 1)
    assert (Solution2().getRightDigit(543) == 3)

    #test getNumDigts
    assert(Solution2().getNumTens(5431) == 0)
    assert(Solution2().getNumTens(5430) == 1)
    assert(Solution2().getNumTens(5400) == 2)

    # test intToRoman
    assert (Solution2().intToRoman(3) == "III")
    assert (Solution2().intToRoman(4) == "IV")
    assert (Solution2().intToRoman(9) == "IX")
    assert (Solution2().intToRoman(58) == "LVIII")
    assert (Solution2().intToRoman(1994) == "MCMXCIV")
    assert (Solution2().intToRoman(123) == "CXXIII")
    assert (Solution2().intToRoman(5431) == "MMMMMCDXXXI")
    assert (Solution2().intToRoman(1000) == "M")
    assert (Solution2().intToRoman(10999) == "MMMMMMMMMMCMXCIX")
    assert (Solution2().intToRoman(20999) == "MMMMMMMMMMMMMMMMMMMMCMXCIX")

    #Solution 3
    #test right most digit
    assert(Solution3().getRightDigit(5431) == 1)
    assert (Solution3().getRightDigit(543) == 3)

    # test intToRoman
    assert (Solution3().intToRoman(3) == "III")
    assert (Solution3().intToRoman(4) == "IV")
    assert (Solution3().intToRoman(9) == "IX")
    assert (Solution3().intToRoman(58) == "LVIII")
    assert (Solution3().intToRoman(1994) == "MCMXCIV")
    assert (Solution3().intToRoman(123) == "CXXIII")
    assert (Solution3().intToRoman(5431) == "MMMMMCDXXXI")
    assert (Solution3().intToRoman(1000) == "M")
    assert (Solution3().intToRoman(10999) == "MMMMMMMMMMCMXCIX")
    assert (Solution3().intToRoman(20999) == "MMMMMMMMMMMMMMMMMMMMCMXCIX")