class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # maps rows to their contents
        row_buckets = {};
        # direction flat, counts numbers up, false counts numbers down
        forward_dir = True;
        str_idx = 0;

        for char in s:

            # make bucket if no bucket for index exists
            if row_buckets.get(str_idx) is None:
                row_buckets[str_idx] = [];

            # add
            print("%s inserted into row %d bucket" % (char, str_idx))
            row_buckets[str_idx].append(char)

            if forward_dir:
                str_idx += 1
            else:
                str_idx -= 1

            # check if we need to reverse direction
            if str_idx == (numRows - 1):
                forward_dir = False
            elif str_idx == 0:
                forward_dir = True

        # join all the buckets
        result = []
        for key in row_buckets.keys():
            result.extend(row_buckets[key])

        print(result)
        return ''.join(result)


if __name__ == "__main__":

    output = Solution().convert("PAYPALISHIRING", 3)
    print(output)
    assert (output == "PAHNAPLSIIGYIR")

    output = Solution().convert("PAYPALISHIRING", 4)
    print(output)
    assert (output == "PINALSIGYAHRPI")

    output = Solution().convert("btruqecgbdibodvshoxaxksyhbrxxrfbkyvccaifftgtwendulfrxyrebjeaajbljzplzyseryzpenuyazszxldyujzvucid", 2)
    print(output)
