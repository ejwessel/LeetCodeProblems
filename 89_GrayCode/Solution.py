from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:

        # if 0 bits, we still need an output
        if n == 0:
            result = [0]
            # print(result)
            return result

        list = ['']

        for i in range(n):
            right = list.copy()
            right.reverse()
            list = list + right
            # prepend the first half with 0's
            for b in range(0, int(len(list) / 2)):
                list[b] = '0' + list[b]

            # prepend the second half with 1's
            for b in range(int(len(list) / 2), len(list)):
                list[b] = '1' + list[b]

        # print(list)

        output = []
        for binary in list:
            output.append(int(binary, 2))
        return output

if __name__ == "__main__":
    sol = Solution()

    result = sol.grayCode(0)
    assert result == [0]

    result = sol.grayCode(1)
    assert result == [0, 1]

    result = sol.grayCode(2)
    assert result == [0, 1, 3, 2]

    result = sol.grayCode(3)
    assert result == [0, 1, 3, 2, 6, 7, 5, 4]

    result = sol.grayCode(4)
    assert result == [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
