class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_i = len(a) - 1
        b_i = len(b) - 1
        carry = 0
        answer = ""
        while a_i >= 0 and b_i >= 0:
            summed = int(a[a_i]) + int(b[b_i]) + carry
            val = summed % 2
            carry = summed // 2
            answer = str(val) + answer
            a_i -= 1
            b_i -= 1

        # handle left overs
        while a_i >= 0:
            summed = int(a[a_i]) + carry
            val = summed % 2
            carry = summed // 2
            answer = str(val) + answer
            a_i -= 1

        while b_i >= 0:
            summed = int(b[b_i]) + carry
            val = summed % 2
            carry = summed // 2
            answer = str(val) + answer
            b_i -= 1

        #handle left over carry
        if carry == 1:
            answer = "1" + answer

        return answer

if __name__ == "__main__":
    sol = Solution()
    result = sol.addBinary("1", "1")
    assert result == "10"

    result = sol.addBinary("1", "0")
    assert result == "1"

    result = sol.addBinary("0", "1")
    assert result == "1"

    result = sol.addBinary("10", "1")
    assert result == "11"

    result = sol.addBinary("101", "1")
    assert result == "110"

    result = sol.addBinary("1010", "1011")
    assert result == "10101"
