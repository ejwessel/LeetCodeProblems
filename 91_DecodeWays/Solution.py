num_to_letters = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    '10': 'J',
    '11': 'K',
    '12': 'L',
    '13': 'M',
    '14': 'N',
    '15': 'O',
    '16': 'P',
    '17': 'Q',
    '18': 'R',
    '19': 'S',
    '20': 'T',
    '21': 'U',
    '22': 'V',
    '23': 'W',
    '24': 'X',
    '25': 'Y',
    '26': 'Z',
}


class Solution:
    def numDecodings(self, s: str):

        if int(s[0]) == 0:
            return 0

        prev_list = []
        for i in reversed(range(len(s))):
            if s[i] == '0':
                prev_list.append(0)
            elif len(prev_list) == 0:
                prev_list.append(1)
            elif len(prev_list) == 1:
                if s[i] in num_to_letters and s[i] + s[i + 1] in num_to_letters:
                    if prev_list[0] > 0:
                        prev_list.append(prev_list[0] + prev_list[0])
                    else:
                        prev_list.append(1)
                elif s[i] in num_to_letters:
                    prev_list.append(prev_list[0])
            else:
                if s[i] in num_to_letters and s[i] + s[i + 1] in num_to_letters:
                    prev_list.append(prev_list[0] + prev_list[1])
                elif s[i] in num_to_letters:
                    prev_list.append(prev_list[1])

            # reduce queue if greater than allowed size
            if len(prev_list) > 2:
                prev_list = prev_list[1:]


        # the last element is the number of ways decoded
        if len(prev_list) == 1:
            return prev_list[0]
        return prev_list[1]


if __name__ == "__main__":
    sol = Solution()
    result = sol.numDecodings('129')
    assert result == 2

    result = sol.numDecodings('1010')
    assert result == 1

    result = sol.numDecodings('100')
    assert result == 0

    result = sol.numDecodings('10')
    assert result == 1

    result = sol.numDecodings('999')
    assert result == 1

    result = sol.numDecodings('1')
    assert result == 1

    result = sol.numDecodings('0')
    assert result == 0

    result = sol.numDecodings('01')
    assert result == 0

    result = sol.numDecodings('12')
    assert result == 2

    result = sol.numDecodings('111')
    assert result == 3

    result = sol.numDecodings('1111')
    assert result == 5

    result = sol.numDecodings('11111')
    assert result == 8

    result = sol.numDecodings('111111')
    assert result == 13

    result = sol.numDecodings('2226')
    assert result == 5

    result = sol.numDecodings('7226')
    assert result == 3

    result = sol.numDecodings('62226')
    assert result == 5

    result = sol.numDecodings('207226')
    assert result == 3

    result = sol.numDecodings('11016')
    assert result == 2

    result = sol.numDecodings('102')
    assert result == 1

    result = sol.numDecodings('226')
    assert result == 3

    result = sol.numDecodings('9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253')
    assert result == 3981312

